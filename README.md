# OpenAI PCM16 Audio Player

This project provides a frontend solution to decode and play PCM16 audio frames received from OpenAI's API.

## Features

- Decode base64-encoded PCM16 audio data
- Convert PCM16 to browser-compatible audio formats
- Play audio using Web Audio API
- Fallback audio element for broader compatibility
- Sample audio generation for testing

## Usage

1. Open `index.html` in a web browser
2. Paste the base64-encoded PCM16 audio data from OpenAI into the textarea
3. Click "Play Audio" to decode and play the audio
4. Use "Load Sample Data" to test with generated audio

## Technical Details

### Audio Format Support
- **Input**: PCM16 (16-bit signed integers) at 24kHz sample rate
- **Output**: Web Audio API AudioBuffer and WAV file format
- **Channels**: Mono (1 channel)

### Browser Compatibility
- Modern browsers supporting Web Audio API
- Fallback to HTML5 audio element
- Requires HTTPS for microphone access (if needed)

## Integration with OpenAI

When receiving audio from OpenAI's realtime API:

```javascript
// Example WebSocket message handling
websocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (data.type === 'response.audio.delta') {
        // Accumulate base64 audio data
        accumulatedAudio += data.delta;
    } else if (data.type === 'response.audio.done') {
        // Play the complete audio
        audioPlayer.playPCM16FromBase64(accumulatedAudio);
        accumulatedAudio = '';
    }
};
```

## File Structure

- `index.html` - Main HTML interface
- `audio-player.js` - PCM16 audio decoding and playback logic
- `README.md` - This documentation

## Troubleshooting

### No Audio Output
1. Check browser console for errors
2. Ensure audio data is valid base64
3. Try the sample data first
4. Check if browser blocks autoplay

### Browser Compatibility Issues
- Use Chrome/Firefox for best Web Audio API support
- Enable autoplay permissions if needed
- For mobile, user interaction is required before audio playback