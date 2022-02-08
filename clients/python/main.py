from dotenv import load_dotenv
import os
import asyncio
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
load_dotenv()


async def main():

    endpoint = os.environ.get("GRAPH_ENDPOINT")

    transport = AIOHTTPTransport(url=endpoint)

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
        # id ID!, from Bytes!, to Bytes!, value BigInt!
        query = gql(
        """
            {
                punkBids {
                    id
                    index
                    value
                    from
                }
            }
        """
        )

        result = await session.execute(query)
        print(result)


asyncio.run(main())
