# Graph Starter

Deploy a decentralized GraphQL API with the [Graph](https://thegraph.com/).

![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

## Setup

Prerequisites:
- Graph CLI (`npm install -g @graphprotocol/graph-cli`)
- Ethereum archive node HTTP API key (Get one [here](https://www.alchemy.com/))

1. **Start the Ethereum mainnet fork node:** Open a terminal and run the following:

    ```shell
    npm i
    npx hardhat node --fork https://eth-mainnet.alchemyapi.io/v2/<your-key>
    ```

    You'll want to leave this node running for the rest of the process.

2. **Start the Graph node:** Open another terminal, change directory to [node/docker](node/docker) and run:

    ```shell
    cd node/docker
    docker-compose up
    ```

    You'll also want to leave this node running for the rest of the process.

    **Note:** Whenever the Ethereum network has been reset (eg. Hardhat restarted, computer rebooted…), you must DELETE the ./docker/data folder located in the node folder cloned from the repository).
    This is required to clean the existing database that checks the genesis block for the current Ethereum network. You can do this cleanup by running `rm -rf "graph/node/docker/data"`. You can stop the node anytime by running `CTRL+C` in the terminal that you started it in.

3. **Update the contract ABI:** In [subgraph/abis/Contract.json](subgraph/abis/Contract.json), replace the existing json with your contract ABI json.

4. **Update the contract address:** In [subgraph/subgraph.yaml](subgraph/subgraph.yaml), change `dataSources:source:address:` to your contract address.

5. **Build and deploy the subgraph:** Change directory to [subgraph](subgraph) and run the following to create and deploy the subgraph your local Graph node:

    ```shell
    cd subgraph
    npm run codegen
    npm run build
    npm run create-local
    npm run deploy-local
    ```

    The last command should output both an HTTP and a WS endpoint for your subgraph. ***Save your HTTP endpoint as `GRAPH_ENDPOINT`  in your `.env` file for testing queries.***

6. **Test your endpoint:** Try it with [clients/python/main.py](clients/python/main.py).

## Example Contract

Try the contract at `https://etherscan.io/address/0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB#code`. 

![Cryptopunk #7523](assets/cryptopunk.png)

Pictures: a cryptopunk that is worth $11.75 million. We can index a history of bid and buy events for this 'punk.

1. Scroll down to the section titled `Contract ABI` and copy the ABI json. Paste this into [subgraph/abis/Contract.json](subgraph/abis/Contract.json), as mentioned in step 2 above.

2. Copy the contract address from Etherscan. Paste this into `dataSources:source:address:` in [subgraph/subgraph.yaml](subgraph/subgraph.yaml), as mentioned in step 3 above.

3. Run step 4 above to create and deploy the subgraph.

4. Install the python dependencies for [client](client) as you prefer and run the following to test your subgraph endpoint:

    ```shell
    pip install -r requirements.txt
    python main.py
    ```

    You should see a history of transfers for the contract.



