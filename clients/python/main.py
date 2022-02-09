from dotenv import load_dotenv
import os
import asyncio
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
load_dotenv()


async def main():

    endpoint = os.environ.get("GRAPH_ENDPOINT")

    transport = AIOHTTPTransport(url=endpoint)

    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
        # id ID!, index BigInt!, value BigInt!, from Bytes!, to Bytes! 
        query = gql("""
            {
                punkBids(subgraphError: allow) {
                    id
                    index
                    value
                    from
                }
            }
        """)
            # Alternatively, you could use the following query string:
            # {
            #     punkBuys(subgraphError: allow) {
            #         id
            #         index
            #         value
            #         from
            #         to
            #     }
            # }

        result = await session.execute(query)
        print(result)


asyncio.run(main())
