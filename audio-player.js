class PCM16AudioPlayer {
    constructor() {
        this.audioContext = null;
        this.currentSource = null;
        this.sampleRate = 24000; // OpenAI typically uses 24kHz for PCM16
        this.channels = 1; // Mono audio
    }

    async initAudioContext() {
        if (!this.audioContext) {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
        
        // Resume audio context if suspended
        if (this.audioContext.state === 'suspended') {
            await this.audioContext.resume();
        }
    }

    base64ToArrayBuffer(base64) {
        const binaryString = window.atob(base64);
        const len = binaryString.length;
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) {
            bytes[i] = binaryString.charCodeAt(i);
        }
        return bytes.buffer;
    }

    pcm16ToFloat32Array(arrayBuffer) {
        const dataView = new DataView(arrayBuffer);
        const length = arrayBuffer.byteLength / 2; // 16-bit = 2 bytes per sample
        const float32Array = new Float32Array(length);
        
        for (let i = 0; i < length; i++) {
            // Read 16-bit signed integer (little-endian)
            const sample = dataView.getInt16(i * 2, true);
            // Convert to float32 (-1.0 to 1.0)
            float32Array[i] = sample / 32768.0;
        }
        
        return float32Array;
    }

    createWAVHeader(length, sampleRate, channels) {
        const buffer = new ArrayBuffer(44);
        const view = new DataView(buffer);
        
        // WAV header
        const writeString = (offset, string) => {
            for (let i = 0; i < string.length; i++) {
                view.setUint8(offset + i, string.charCodeAt(i));
            }
        };
        
        writeString(0, 'RIFF');                                    // ChunkID
        view.setUint32(4, 36 + length * 2, true);                 // ChunkSize
        writeString(8, 'WAVE');                                    // Format
        writeString(12, 'fmt ');                                   // Subchunk1ID
        view.setUint32(16, 16, true);                              // Subchunk1Size
        view.setUint16(20, 1, true);                               // AudioFormat (PCM)
        view.setUint16(22, channels, true);                        // NumChannels
        view.setUint32(24, sampleRate, true);                      // SampleRate
        view.setUint32(28, sampleRate * channels * 2, true);       // ByteRate
        view.setUint16(32, channels * 2, true);                    // BlockAlign
        view.setUint16(34, 16, true);                              // BitsPerSample
        writeString(36, 'data');                                   // Subchunk2ID
        view.setUint32(40, length * 2, true);                      // Subchunk2Size
        
        return buffer;
    }

    createWAVBlob(pcmData) {
        const length = pcmData.length;
        const header = this.createWAVHeader(length, this.sampleRate, this.channels);
        const wav = new ArrayBuffer(header.byteLength + pcmData.byteLength);
        
        // Copy header
        new Uint8Array(wav, 0, header.byteLength).set(new Uint8Array(header));
        
        // Copy PCM data
        new Uint8Array(wav, header.byteLength).set(new Uint8Array(pcmData));
        
        return new Blob([wav], { type: 'audio/wav' });
    }

    async playPCM16FromBase64(base64Data) {
        try {
            await this.initAudioContext();
            
            // Remove any whitespace and data URL prefix
            const cleanBase64 = base64Data.trim().replace(/^data:audio\/[^;]+;base64,/, '');
            
            // Convert base64 to ArrayBuffer
            const arrayBuffer = this.base64ToArrayBuffer(cleanBase64);
            
            if (arrayBuffer.byteLength === 0) {
                throw new Error('No audio data found');
            }
            
            // Method 1: Use Web Audio API directly
            const float32Data = this.pcm16ToFloat32Array(arrayBuffer);
            const audioBuffer = this.audioContext.createBuffer(
                this.channels, 
                float32Data.length, 
                this.sampleRate
            );
            
            // Copy the audio data to the buffer
            audioBuffer.copyToChannel(float32Data, 0);
            
            // Create and configure the audio source
            const source = this.audioContext.createBufferSource();
            source.buffer = audioBuffer;
            source.connect(this.audioContext.destination);
            
            // Stop any currently playing audio
            this.stop();
            this.currentSource = source;
            
            // Play the audio
            source.start(0);
            
            // Method 2: Also create a downloadable WAV file for the audio element
            const wavBlob = this.createWAVBlob(arrayBuffer);
            const audioUrl = URL.createObjectURL(wavBlob);
            const audioElement = document.getElementById('audioElement');
            audioElement.src = audioUrl;
            audioElement.style.display = 'block';
            
            return {
                duration: audioBuffer.duration,
                sampleRate: this.sampleRate,
                channels: this.channels,
                samples: float32Data.length
            };
            
        } catch (error) {
            console.error('Error playing PCM16 audio:', error);
            throw error;
        }
    }

    stop() {
        if (this.currentSource) {
            try {
                this.currentSource.stop();
            } catch (e) {
                // Source might already be stopped
            }
            this.currentSource = null;
        }
        
        const audioElement = document.getElementById('audioElement');
        audioElement.pause();
        audioElement.currentTime = 0;
    }
}

// Global player instance
const audioPlayer = new PCM16AudioPlayer();

// UI functions
function showStatus(message, type = 'info') {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = message;
    statusDiv.className = `status ${type}`;
    statusDiv.style.display = 'block';
    
    // Auto-hide after 5 seconds for success messages
    if (type === 'success') {
        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 5000);
    }
}

async function playAudio() {
    const audioData = document.getElementById('audioData').value.trim();
    const playBtn = document.getElementById('playBtn');
    const stopBtn = document.getElementById('stopBtn');
    
    if (!audioData) {
        showStatus('Please paste base64 audio data first', 'error');
        return;
    }
    
    try {
        playBtn.disabled = true;
        stopBtn.disabled = false;
        showStatus('Decoding and playing audio...', 'info');
        
        const info = await audioPlayer.playPCM16FromBase64(audioData);
        
        showStatus(
            `Audio playing! Duration: ${info.duration.toFixed(2)}s, ` +
            `Sample Rate: ${info.sampleRate}Hz, ` +
            `Samples: ${info.samples}`, 
            'success'
        );
        
    } catch (error) {
        showStatus(`Error: ${error.message}`, 'error');
        console.error('Playback error:', error);
    } finally {
        playBtn.disabled = false;
    }
}

function stopAudio() {
    audioPlayer.stop();
    document.getElementById('stopBtn').disabled = true;
    showStatus('Audio stopped', 'info');
}

function loadSampleData() {
    // Create a small sample PCM16 data (silence with a brief tone)
    const sampleRate = 24000;
    const duration = 1; // 1 second
    const samples = sampleRate * duration;
    const buffer = new ArrayBuffer(samples * 2);
    const view = new DataView(buffer);
    
    // Generate a simple sine wave tone
    for (let i = 0; i < samples; i++) {
        const t = i / sampleRate;
        const frequency = 440; // A4 note
        const amplitude = 0.3;
        const sample = Math.sin(2 * Math.PI * frequency * t) * amplitude;
        const pcm16Sample = Math.round(sample * 32767);
        view.setInt16(i * 2, pcm16Sample, true);
    }
    
    // Convert to base64
    const uint8Array = new Uint8Array(buffer);
    const base64 = btoa(String.fromCharCode.apply(null, uint8Array));
    
    document.getElementById('audioData').value = base64;
    showStatus('Sample PCM16 data loaded (440Hz tone)', 'success');
}

// Handle audio element events
document.addEventListener('DOMContentLoaded', function() {
    const audioElement = document.getElementById('audioElement');
    
    audioElement.addEventListener('ended', function() {
        document.getElementById('stopBtn').disabled = true;
        showStatus('Audio playback completed', 'success');
    });
    
    audioElement.addEventListener('error', function(e) {
        showStatus('Audio element error: ' + e.message, 'error');
    });
});

// Export for potential use in other scripts
window.PCM16AudioPlayer = PCM16AudioPlayer;