from solana.rpc.api import Client

# Solana Devnet RPC URL
RPC_URL = "https://api.devnet.solana.com"

def connect_to_rpc():
    # Initialize the Solana RPC client
    client = Client(RPC_URL)

    # Check if the connection is successful
    try:
        response = client.is_connected()
        if response:
            print("Successfully connected to the Solana devnet RPC node.")
        else:
            print("Failed to connect to the Solana devnet RPC node.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    connect_to_rpc()
