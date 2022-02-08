# Graph Starter

## Setup

Prerequisites:
- Graph CLI (`npm install -g @graphprotocol/graph-cli`)

1. Open a terminal, change directory to [node/docker](node/docker) and start The Graph node (you'll want to leave it running for the rest of the process):

    ```shell
    cd node/docker
    docker-compose up
    ```

    Wait for deployment logs to complete and confirm your node is running before continuing. 

    **Note:** Whenever the Ethereum network has been reset (eg. Hardhat restarted, computer rebooted…), you must DELETE the ./docker/data folder located in the node folder cloned from the repository).
    This is required to clean the existing database that checks the genesis block for the current Ethereum network. You can do this cleanup by running `rm -rf "graph/node/docker/data"`. You can stop the node anytime by running `CTRL+C` in the terminal that you started it in.

2. In [subgraph/abis/Contract.json](subgraph/abis/Contract.json), replace the existing json with your contract ABI json.

3. In [subgraph/subgraph.yaml](subgraph/subgraph.yaml), change `dataSources:source:address:` to your contract address.

4. Change directory to [subgraph](subgraph) and run the following to create and deploy the subgraph your local Graph node:

    ```shell
    cd subgraph
    npm run codegen
    npm run build
    npm run create-local
    npm run deploy-local
    ```

    The last command should output an HTTP and WS endpoint for your subgraph. Saved your HTTP endpoint as `GRAPH_ENDPOINT`  in your `.env` file for testing queries.

5. Test your endpoint in [client/main.py](client/main.py).

## Example Contract

Try the contract at `https://etherscan.io/address/0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB#code`. It's for a cryptopunk that is worth $11.75 million.

1. Scroll down to the section titled `Contract ABI` and copy the ABI json. Paste this into [subgraph/abis/Contract.json](subgraph/abis/Contract.json), as mentioned in step 2 above.

2. Copy the contract address from Etherscan. Paste this into `dataSources:source:address:` in [subgraph/subgraph.yaml](subgraph/subgraph.yaml), as mentioned in step 3 above.

3. Run step 4 above to create and deploy the subgraph.

4. Install the python dependencies for [client](client) as you prefer and run the following to test your subgraph endpoint:

    ```shell
    pip install -r requirements.txt
    python main.py
    ```

    You should see a history of transfers for the contract.



