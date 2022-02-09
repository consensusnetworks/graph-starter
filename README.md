# Graph Starter

Deploy a decentralized GraphQL API with the [Graph](https://thegraph.com/).

![The Graph image](assets/graph.webp)

![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

## Prerequisites

You'll need a few things:
- Graph CLI (`npm install -g @graphprotocol/graph-cli`)
- Ethereum archive node HTTP API key (from [Alchemy](https://www.alchemy.com/))
- Docker, Python and Node

## Setup

The setup task is to start a local Ethereum node as a fork of the existing mainnet to have easy access to rich public on-chain data, and to start a local Graph node to deploy and test a GraphQL API.

1. Open a terminal and install dependencies for the starter:
   ```shell
    npm install
    ```
   
2. Now run the following to start an Ethereum mainnet fork node:
    ```shell
    npx hardhat node --fork https://eth-mainnet.alchemyapi.io/v2/<your-key>
    ```
    You'll want to leave this node running for the rest of the process.

3. Open another terminal, change directory to [node/docker](node/docker) and run the following to start a Graph node:
    ```shell
    cd node/docker
    docker-compose up
    ```
    You'll also want to leave this node running for the rest of the process. **Note:** Whenever the Ethereum network has been reset (eg. Hardhat restarted, computer rebooted…), you must DELETE the ./docker/data folder located in the node folder cloned from the repository).
    This is required to clean the existing database that checks the genesis block for the current Ethereum network. You can do this cleanup by running `rm -rf "graph/node/docker/data"`. You can stop the node anytime by running `CTRL+C` in the terminal that you started it in.

## Usage

You'll need a contract ABI json and address to get started with a new subgraph. To start, you can use the example values provided.

### Example

We can deploy our example that looks at [the contract for CryptoPunk #7523](https://etherscan.io/address/0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB#code). 

![Cryptopunk #7523](assets/cryptopunk.png)

*Pictured above: A cryptopunk that is worth $11.75 million. We can index a history of bid and buy events for this 'punk.*

1. Take a look at [subgraph/schema.graphql](subgraph/schema.graphql), [subgraph/src/mapping.ts](subgraph/src/mapping.ts) and [subgraph/subgraph.yaml](subgraph/subgraph.yaml) to our entity schema, our event handlers, and our data sources, respectively. You can also check out [clients/python/main.py](clients/python/main.py) to see the desired GraphQL API.  

2. Change directory to [subgraph](subgraph) and run the following to create and deploy the example subgraph your local Graph node:
    ```shell
    cd subgraph
    npm run codegen
    npm run build
    npm run create-local
    npm run deploy-local
    ```
    The last command should output both an HTTP and a WS endpoint for your subgraph. **Save your HTTP endpoint as `GRAPH_ENDPOINT`  in your `.env` file for testing queries.** For this setup, the default should be `http://127.0.0.1:8000/subgraphs/name/consensusnetworks/graph-starter`.

3. Test your endpoint at the local url provided by the terminal for your GraphQL server. You should be able to run the expected queries in the GraphiQL sandbox. 
    **Note:** If you are using a contract that has a very long history on-chain, you may need to wait a few minutes for the data to be indexed... or hours (if you're on a slow internet connection). *Don't fear, once things are indexed you will find speed is very fast.*

4. Change directory to [clients/python](clients/python) and install the python dependencies as you prefer and run the following to test your subgraph endpoint:
    ```shell
    cd clients/python
    pip install -r requirements.txt
    python3 main.py
    ```
    You should see the terminal print a history of bids and buys for the contract, like this:


### Development

Now you can retrieve your own contract of choice and create a subgraph for it.

1. In [subgraph/abis/Contract.json](subgraph/abis/Contract.json), replace the existing json with your contract ABI json. See how you can find your contract ABI json [here](https://thegraph.com/docs/en/developer/create-subgraph-hosted/#getting-the-ab-is).

2. In [subgraph/subgraph.yaml](subgraph/subgraph.yaml), change `dataSources:source:address:` to your contract address.

3. Change directory to [subgraph](subgraph) and run the subgraph commands from Step 2 in the example above to create and deploy the contract to your node. Make sure to update the `GRAPH_ENDPOINT` in your `.env` file with the new HTTP endpoint provided by the terminal. 

    The commands are repasted below for your convenience:
    ```shell
    cd subgraph
    npm run codegen
    npm run build
    npm run create-local
    npm run deploy-local
    ```

### Deployment

Todo. Deploy to the Graph mainnet. Not really needed for analyzing data internally, but this is a fun aspect of the protocol. Your API can be consumed by anyone.

## Background

Todo. More why on the Graph and why not just build-your-own indexer to a Postgres.

### Subgraphs

Todo. How do they fit into the protocol and community?

### ABIs

Todo. How to inspect what events and data are available on a contract/on-chain. 

### Mappings

Todo. How to index events how you want them with an AssemblyScript mapping.

## What Next?

Find interesting data and use it!

## Contributing

Pull requests targeting the `master` branch are welcome anytime. For major changes, please check out what's already being worked on [here](https://github.com/consensusnetworks/graph-starter/issues) and open a new issue before starting!

## License

[MIT](https://choosealicense.com/licenses/mit/)

   




