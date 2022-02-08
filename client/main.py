from dotenv import load_dotenv
import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

load_dotenv()
endpoint = os.environ.get("GRAPH_ENDPOINT")

transport = AIOHTTPTransport(url=endpoint)
client = Client(transport=transport, fetch_schema_from_transport=True)

# id: ID!, from: Bytes!, to: Bytes!, value: BigInt!
query = gql(
    """
    {
        transfers {
            id
            from
            to
            value
        }
    }
    """
)

result = client.execute(query)
print(result)
