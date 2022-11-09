// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/

// decode payload to JSON
var data = decodeToJson(payload);

var parsedPayload = parsePayloadWS301(data.payload);

// Result object with device/asset attributes/telemetry data
var result = {
// Use deviceName and deviceType or assetName and assetType, but not both.
   deviceName: data.deviceId,
   deviceType: 'reed_sensor',
   telemetry: {
       payload: data.payload,
       battery: parsedPayload.battery,
       rawData: parsedPayload.state,
       install: parsedPayload.install
   }
};

function parsePayloadWS301(payload){
    var decoded = {};

    var bytes = hexToBytes(payload);

    for (var i = 0; i < bytes.length; ) {
        var channel_id = bytes[i++];
        var channel_type = bytes[i++];
        // BATTERY
        if (channel_id === 0x01 && channel_type === 0x75) {
            decoded.battery = bytes[i];
            i += 1;
        }
        // DOOR / WINDOW STATE (0: close 1: open)
        else if (channel_id === 0x03 && channel_type === 0x00) {
            decoded.state = bytes[i] === 0 ? "close" : "open";
            i += 1;
        }
        // INSTALL STATE (0: install 1: uninstall)
        else if (channel_id === 0x04 && channel_type === 0x00) {
            decoded.install = bytes[i] === 0 ? "yes" : "no";
            i += 1;
        } else {
            break;
        }
    }

    return decoded;
}

function hexToBytes(hex) {
    for (var bytes = [], c = 0; c < hex.length; c += 2)
        bytes.push(parseInt(hex.substr(c, 2), 16));
    return bytes;
}

/** Helper functions **/

function decodeToString(payload) {
   return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
   // covert payload to string.
   var str = decodeToString(payload);

   // parse string to JSON
   var data = JSON.parse(str);
   return data;
}

return result;