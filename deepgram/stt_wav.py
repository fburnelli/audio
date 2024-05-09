# Copyright 2023-2024 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

import logging, verboselogs
from time import sleep
import os
from dotenv import load_dotenv
from datetime import datetime
import httpx
import json

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
    FileSource,
    PrerecordedOptions
)

AUDIO_FILE = "../../data/test.wav"

with open('../../data/deepgram.key', 'r') as file:
    content = file.read()
DEEPGRAM_API_KEY = content.strip()

deepgram: DeepgramClient = DeepgramClient(DEEPGRAM_API_KEY)


with open(AUDIO_FILE, "rb") as file:
    buffer_data = file.read()

payload: FileSource = {            "buffer": buffer_data,}

options: PrerecordedOptions = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            utterances=True,
            punctuate=True,
            diarize=True,
        )

before = datetime.now()
response = deepgram.listen.prerecorded.v("1").transcribe_file(
            payload, options, timeout=httpx.Timeout(300.0, connect=10.0)
        )
after = datetime.now()

#print(response.to_json(indent=4))

print(f"duration:{response.metadata.duration}")
print(f"channels:{response.metadata.channels}")
print(f"model:{response.metadata.model_info}")

resp = response.to_json()
res = json.loads(resp).get("results")
channels = res.get("channels")
transcript = channels[0].get("alternatives")[0].get("transcript")
print(f"trx:{transcript }")
print(channels[0].get("paragraphs"))
for utterance in res.get("utterances"):
    print(f'channel:{utterance.get("channel"):>10} {utterance.get("start"):>10} {utterance.get("end"):>10}  {utterance.get("transcript"):<50}')

input(11111)





{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "d1cdecd3-f90f-4756-81f4-109aa79605f9",
        "sha256": "f47a2223dbfda0b9677f94e4d6a1b88e262095e86d67f4a25baec9d5a2f0b418",
        "created": "2024-04-26T13:55:05.888Z",
        "duration": 5.72525,
        "channels": 1,
        "models": [
            "30089e05-99d1-4376-b32e-c263170674af"
        ],
        "model_info": {
            "30089e05-99d1-4376-b32e-c263170674af": {
                "name": "2-general-nova",
                "version": "2024-01-09.29447",
                "arch": "nova-2"
            }
        }
    },
    "results": {
        "channels": [
            {
                "alternatives": [
                    {
                        "transcript": "But it is not used compact. So utilization density is very important as well.",
                        "confidence": 0.9989029,
                        "words": [
                            {
                                "word": "but",
                                "start": 0.08,
                                "end": 0.39999998,
                                "confidence": 0.7523455,
                                "punctuated_word": "But",
                                "speaker": 0,
                                "speaker_confidence": 0.99853516
                            },
                            {
                                "word": "it",
                                "start": 0.39999998,
                                "end": 0.48,
                                "confidence": 0.99949956,
                                "punctuated_word": "it",
                                "speaker": 0,
                                "speaker_confidence": 0.99853516
                            },
                            {
                                "word": "is",
                                "start": 0.48,
                                "end": 0.71999997,
                                "confidence": 0.999689,
                                "punctuated_word": "is",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "not",
                                "start": 0.71999997,
                                "end": 1.04,
                                "confidence": 0.9998197,
                                "punctuated_word": "not",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "used",
                                "start": 1.04,
                                "end": 1.36,
                                "confidence": 0.9960975,
                                "punctuated_word": "used",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "compact",
                                "start": 1.36,
                                "end": 1.86,
                                "confidence": 0.7430655,
                                "punctuated_word": "compact.",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "so",
                                "start": 2.2,
                                "end": 2.7,
                                "confidence": 0.9406862,
                                "punctuated_word": "So",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "utilization",
                                "start": 3.04,
                                "end": 3.54,
                                "confidence": 0.9951368,
                                "punctuated_word": "utilization",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "density",
                                "start": 3.76,
                                "end": 4.24,
                                "confidence": 0.9886474,
                                "punctuated_word": "density",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "is",
                                "start": 4.24,
                                "end": 4.48,
                                "confidence": 0.99985194,
                                "punctuated_word": "is",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "very",
                                "start": 4.48,
                                "end": 4.7999997,
                                "confidence": 0.9989029,
                                "punctuated_word": "very",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "important",
                                "start": 4.7999997,
                                "end": 5.2,
                                "confidence": 0.99995196,
                                "punctuated_word": "important",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "as",
                                "start": 5.2,
                                "end": 5.3599997,
                                "confidence": 0.99983644,
                                "punctuated_word": "as",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            },
                            {
                                "word": "well",
                                "start": 5.3599997,
                                "end": 5.72525,
                                "confidence": 0.99765384,
                                "punctuated_word": "well.",
                                "speaker": 0,
                                "speaker_confidence": 0.9980469
                            }
                        ],
                        "paragraphs": {
                            "transcript": "\nSpeaker 0: But it is not used compact. So utilization density is very important as well.",
                            "paragraphs": [
                                {
                                    "sentences": [
                                        {
                                            "text": "But it is not used compact.",
                                            "start": 0.08,
                                            "end": 1.86
                                        },
                                        {
                                            "text": "So utilization density is very important as well.",
                                            "start": 2.2,
                                            "end": 5.72525
                                        }
                                    ],
                                    "start": 0.08,
                                    "end": 5.72525,
                                    "num_words": 14,
                                    "speaker": 0
                                }
                            ]
                        }
                    }
                ]
            }
        ],
        "utterances": [
            {
                "start": 0.08,
                "end": 1.86,
                "confidence": 0.9150861,
                "channel": 0,
                "transcript": "But it is not used compact.",
                "words": [
                    {
                        "word": "but",
                        "start": 0.08,
                        "end": 0.39999998,
                        "confidence": 0.7523455,
                        "punctuated_word": "But",
                        "speaker": 0,
                        "speaker_confidence": 0.99853516
                    },
                    {
                        "word": "it",
                        "start": 0.39999998,
                        "end": 0.48,
                        "confidence": 0.99949956,
                        "punctuated_word": "it",
                        "speaker": 0,
                        "speaker_confidence": 0.99853516
                    },
                    {
                        "word": "is",
                        "start": 0.48,
                        "end": 0.71999997,
                        "confidence": 0.999689,
                        "punctuated_word": "is",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "not",
                        "start": 0.71999997,
                        "end": 1.04,
                        "confidence": 0.9998197,
                        "punctuated_word": "not",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "used",
                        "start": 1.04,
                        "end": 1.36,
                        "confidence": 0.9960975,
                        "punctuated_word": "used",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "compact",
                        "start": 1.36,
                        "end": 1.86,
                        "confidence": 0.7430655,
                        "punctuated_word": "compact.",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    }
                ],
                "speaker": 0,
                "id": "9d4adf0e-2c57-4044-a5d7-b07e701a6e66"
            },
            {
                "start": 2.2,
                "end": 2.7,
                "confidence": 0.9406862,
                "channel": 0,
                "transcript": "So",
                "words": [
                    {
                        "word": "so",
                        "start": 2.2,
                        "end": 2.7,
                        "confidence": 0.9406862,
                        "punctuated_word": "So",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    }
                ],
                "speaker": 0,
                "id": "2d3e9bfc-4c31-43ab-8b82-4aed1a6b25a0"
            },
            {
                "start": 3.04,
                "end": 5.72525,
                "confidence": 0.9971402,
                "channel": 0,
                "transcript": "utilization density is very important as well.",
                "words": [
                    {
                        "word": "utilization",
                        "start": 3.04,
                        "end": 3.54,
                        "confidence": 0.9951368,
                        "punctuated_word": "utilization",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "density",
                        "start": 3.76,
                        "end": 4.24,
                        "confidence": 0.9886474,
                        "punctuated_word": "density",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "is",
                        "start": 4.24,
                        "end": 4.48,
                        "confidence": 0.99985194,
                        "punctuated_word": "is",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "very",
                        "start": 4.48,
                        "end": 4.7999997,
                        "confidence": 0.9989029,
                        "punctuated_word": "very",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "important",
                        "start": 4.7999997,
                        "end": 5.2,
                        "confidence": 0.99995196,
                        "punctuated_word": "important",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "as",
                        "start": 5.2,
                        "end": 5.3599997,
                        "confidence": 0.99983644,
                        "punctuated_word": "as",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    },
                    {
                        "word": "well",
                        "start": 5.3599997,
                        "end": 5.72525,
                        "confidence": 0.99765384,
                        "punctuated_word": "well.",
                        "speaker": 0,
                        "speaker_confidence": 0.9980469
                    }
                ],
                "speaker": 0,
                "id": "28ac0808-dd59-488b-8278-0a362e862565"
            }
        ]
    }
}