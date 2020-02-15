"""Initializing client"""
import asyncio


async def tcp_echo_client():
    """Sending data to server"""
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    try:
        while True:
            command = input(">> ")
            if command == 'exit':
                print('Bye Bye\nClose the connection')
                break
            else:
                writer.write(command.encode())
                data = await reader.read(10000)
                print(f'Response: {data.decode()}')
    except ConnectionResetError:
        print('''The Server is disconnected, Please run the application again
Sorry for inconvenience''')
    except ConnectionError:
        print('''The Server is disconnected, Please run the application again
Sorry for inconvenience''')
    finally:
        writer.close()


asyncio.run(tcp_echo_client())
