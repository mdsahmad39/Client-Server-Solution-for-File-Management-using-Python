"""Initialization of server"""
import os
import asyncio
import signal

from Main_Directory.user_handling import Commands

signal.signal(signal.SIGINT, signal.SIG_DFL)
USER_INFO = {}

# Clearing login users who disconnected inappropriately in previous session
PATH = os.getcwd()
FILE = open(f"{PATH}//login_users.txt", 'w')
FILE.close()


async def handle_echo(reader, writer):
    """Handling inputs from different clients adn processing them accordingly"""
    client = writer.get_extra_info('peername')
    message = f"{client} is connected !!!!"
    USER_INFO[client[1]] = Commands(client)
    print(message)
    try:
        while True:
            data = await reader.read(10000)
            command = data.decode()
            response = USER_INFO[client[1]].execute(command)
            if response is None or response == '':
                response = '.'
                writer.write(response.encode())
            elif response is not None:
                writer.write(response.encode())
                await writer.drain()
            else:
                if command == 'exit':
                    close_msg = f'{client} wants to close the connection.'
                    print(close_msg)
                    break
                writer.close()
    except ConnectionResetError:
        print(f"The client {client} is disconnected")
    except ConnectionError:
        print(f"The client {client} is disconnected")


async def main():
    """Main program starts execution here"""
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8080)

    client = server.sockets[0].getsockname()
    print(f'Serving on {client}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
