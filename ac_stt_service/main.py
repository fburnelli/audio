# python -m uvicorn main:app --reload


import json

import time

import os

 

from fastapi import FastAPI,APIRouter

from pydantic import BaseModel, Field

from typing import Dict, Any,List

import datetime

import uuid

 

ACTIVITIES_PATH = "activities"

REFRESH_PATH = "refresh"

DISCONNECT_PATH = "disconnect"

 

class TranscriptionPart(BaseModel):

    conversation: str

    participant: str

    text: str

    count: int | None = Field(description="The sequence number of the transcription within the conversation",

                              default=None)

 

class BaseAudioCodesActivity(BaseModel):

    id: str

    timestamp: datetime.datetime

    language: str

    type: str

 

class Participant(BaseModel):

    participant: str

    uriUser: str

    uriHost: str

 

class StartConversationParameters(BaseModel):

    calleeHost: str

    callerHost: str

    participants: List[Participant]

    vaigConversationId: str

 

class StartConversationActivity(BaseAudioCodesActivity):

    name: str

    parameters: StartConversationParameters

 

class MessageActivityParameters(BaseModel):

    confidence: float

    recognitionOutput: Dict[str, Any]  # don't care

    participant: str

    participantUriUser: str

 

class MessageActivity(BaseAudioCodesActivity):

    text: str

    parameters: MessageActivityParameters

 

class EndConversationActivity(BaseModel):

    conversation: str

    reason: str

    reasonCode: str

 

class AudioCodesAPI:

    def __init__(self):

        self.router = APIRouter()

        self.router.add_api_route("/", self.validate_bot, methods=["GET"])

        self.router.add_api_route("/", self.validate_bot, methods=["POST"])

        self.router.add_api_route("/activities", self.create_conversation, methods=["POST"])

        self.router.add_api_route("/refresh", self.create_conversation, methods=["POST"])

        self.router.add_api_route("/disconnect", self.create_conversation, methods=["POST"])

        self.router.add_api_route("/health-check", self.create_conversation, methods=["POST"])

 

    async def validate_bot(self):

        print("[validate_bot]")

        return await self.create_conversation({"a":"test"})

 

    @staticmethod

    async def create_conversation(payload: dict):

        print('[create_conversation]', payload)

 

        return {

            "activitiesURL": ACTIVITIES_PATH,

            "refreshURL": REFRESH_PATH,

            "disconnectURL": DISCONNECT_PATH,

            "expiresSeconds": 120

        }

 

app = FastAPI()

api = AudioCodesAPI()

app.include_router(api.router)




if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)