import re
import requests
from plugins import register, Plugin, Event, logger, Reply, ReplyType
import base64
import json
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import asyncio
import time
import websockets

@register
class Tts(Plugin):
    name = "tts"
    def did_receive_message(self, event: Event):
        pass

    def will_generate_reply(self, event: Event):
        query = event.context.query
        if query == self.config.get("command"):
            event.reply = self.reply()
            event.bypass()

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "Use the command #porn(or whatever you like set with command field in the config) to get a wonderful video"

    def reply(self) -> Reply:
        reply = Reply(ReplyType.TEXT, "Failed to get porn videos")
        try:
            
                respone = requests.get('http://127.0.0.1:8000/tts?text=测试游戏阿拉&speaker=BV426_streaming')
                print(respone)
                reply = Reply(ReplyType.MP3, "mp3")
        except Exception as e:
            logger.error(f"Audio api call error: {e}")
        return reply
    
