// Example integration with OpenAI Realtime API
class OpenAIAudioIntegration {
    constructor() {
        this.audioPlayer = new PCM16AudioPlayer();
        this.websocket = null;
        this.accumulatedAudio = '';
        this.isConnected = false;
    }

    async connect(apiKey) {
        try {
            const url = 'wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01';
            
            this.websocket = new WebSocket(url, [], {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'OpenAI-Beta': 'realtime=v1'
                }
            });

            this.websocket.onopen = () => {
                console.log('Connected to OpenAI Realtime API');
                this.isConnected = true;
                this.initializeSession();
            };

            this.websocket.onmessage = (event) => {
                this.handleMessage(JSON.parse(event.data));
            };

            this.websocket.onclose = () => {
                console.log('Disconnected from OpenAI Realtime API');
                this.isConnected = false;
            };

            this.websocket.onerror = (error) => {
                console.error('WebSocket error:', error);
            };

        } catch (error) {
            console.error('Failed to connect:', error);
        }
    }

    initializeSession() {
        // Configure session for audio output
        const sessionConfig = {
            type: 'session.update',
            session: {
                modalities: ['audio', 'text'],
                voice: 'alloy',
                output_audio_format: 'pcm16',
                turn_detection: {
                    type: 'server_vad',
                    threshold: 0.5,
                    prefix_padding_ms: 300,
                    silence_duration_ms: 200
                }
            }
        };

        this.send(sessionConfig);
    }

    handleMessage(data) {
        console.log('Received from OpenAI:', data.type);

        switch (data.type) {
            case 'response.audio.delta':
                // Accumulate audio chunks
                if (data.delta) {
                    this.accumulatedAudio += data.delta;
                    console.log('Received audio chunk:', data.delta.length, 'chars');
                }
                break;

            case 'response.audio.done':
                // Play the complete audio
                console.log('Audio complete, playing...');
                if (this.accumulatedAudio) {
                    this.playAccumulatedAudio();
                }
                break;

            case 'response.audio_transcript.done':
                console.log('Transcript:', data.transcript);
                break;

            case 'error':
                console.error('OpenAI error:', data.error);
                break;

            default:
                console.log('Unhandled message type:', data.type);
        }
    }

    async playAccumulatedAudio() {
        try {
            if (this.accumulatedAudio) {
                console.log('Playing audio, length:', this.accumulatedAudio.length);
                await this.audioPlayer.playPCM16FromBase64(this.accumulatedAudio);
                this.accumulatedAudio = ''; // Clear after playing
            }
        } catch (error) {
            console.error('Error playing audio:', error);
        }
    }

    send(message) {
        if (this.websocket && this.isConnected) {
            this.websocket.send(JSON.stringify(message));
        }
    }

    sendTextMessage(text) {
        const message = {
            type: 'conversation.item.create',
            item: {
                type: 'message',
                role: 'user',
                content: [
                    {
                        type: 'input_text',
                        text: text
                    }
                ]
            }
        };

        this.send(message);

        // Request a response
        this.send({ type: 'response.create' });
    }

    sendAudioMessage(audioData) {
        const message = {
            type: 'conversation.item.create',
            item: {
                type: 'message',
                role: 'user',
                content: [
                    {
                        type: 'input_audio',
                        audio: audioData // base64 encoded audio
                    }
                ]
            }
        };

        this.send(message);
        this.send({ type: 'response.create' });
    }

    disconnect() {
        if (this.websocket) {
            this.websocket.close();
        }
    }
}

// Example usage
/*
const integration = new OpenAIAudioIntegration();
await integration.connect('your-api-key');

// Send a text message
integration.sendTextMessage('Tell me about inertia');

// The audio response will be automatically played when received
*/