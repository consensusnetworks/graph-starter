# Graph Starter

## Setup

1. Open a terminal and start The Graph node (you'll want to leave it running for the rest of the process):

    ```shell
    cd graph/node/docker
    docker-compose up
    ```

    Wait for deployment logs to complete and confirm your node is running before continuing. 

    **Note:** Whenever the Ethereum network has been reset (eg. Hardhat restarted, computer rebooted…), you must DELETE the ./docker/data folder located in the node folder cloned from the repository).
    This is required to clean the existing database that checks the genesis block for the current Ethereum network. You can do this cleanup by running `rm -rf "graph/node/docker/data"`. You can stop the node anytime by running `CTRL+C` in the terminal that you started it in.

2. In [subgraph/abis/Contract.json](subgraph/abis/Contract.json), replace the existing json with your contract ABI json.

3. In [subgraph/subgraph.yaml](subgraph/subgraph.yaml), change `dataSources:source:address:` to your contract address and `dataSources:mappings:abis` to your contract ABI.

4. Run the following to create and deploy the subgraph your local Graph node:

    ```shell
    cd graph/subgraph
    npm run codegen
    npm run build
    npm run create-local
    npm run deploy-local
    ```

    The last command should output an HTTP and WS endpoint for your subgraph. Saved your HTTP endpoint as `GRAPH_ENDPOINT`  in your `.env` file for testing queries.

5. 