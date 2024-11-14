#!/usr/bin/python3
"""Module that defines web connection"""

from typing import List
from fastapi import WebSocket


class ConnectionManager:
    """Class that defines web socket"""

    def __init__(self):
        """Function that initializes connection"""

        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, client_id: int):
        """Function to connect"""

        websocket.cookies.update({'client_id': client_id})
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Function to disconnect"""

        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Function to send confirmation email"""

        await websocket.send_text(message)

    async def send_personal_json(self, message: dict, websocket: WebSocket):
        """Function to send json token"""

        await websocket.send_json(message)

    async def send_private_message(self, message: str, client_id: int):
        """Function to confirm token"""

        websocket = await self.get_client_websocket(self, client_id)
        if websocket:
            await websocket.send_text(message)

    async def send_private_json(self, message: dict, client_id: int):
        """Function to confirm json token"""

        websocket = await self.get_client_websocket(self, client_id)
        if websocket:
            await websocket.send_json(message)

    async def broadcast(self, message: str):
        """Function to broadcast"""

        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_json(self, message: dict):
        """Function to broadcast json token"""

        for connection in self.active_connections:
            await connection.send_json(message)

    async def get_client_websocket(self, client_id: int):
        """Function to get client websocket"""

        socket = [websocket for websocket in self.active_connections
                  if websocket.cookies.get('client_id') == client_id]
        return socket[0] if len(socket) else None


manager = ConnectionManager()
