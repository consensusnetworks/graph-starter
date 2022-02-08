import {
  PunkBidEntered as PunkBidEnteredEvent,
  PunkBought as PunkBoughtEvent,
} from "../generated/Contract/Contract";
import { PunkBidEntered, PunkBought } from "../generated/schema";

export function handlePunkBidEntered(event: PunkBidEnteredEvent): void {
  let entity = new PunkBidEntered(
    event.transaction.hash.toHex() + "-" + event.logIndex.toString()
  );
  entity.index = event.params.punkIndex;
  entity.value = event.params.value;
  entity.from = event.params.fromAddress;
  entity.save();
}

export function handlePunkBought(event: PunkBoughtEvent): void {
  let entity = new PunkBought(
    event.transaction.hash.toHex() + "-" + event.logIndex.toString()
  );
  entity.index = event.params.punkIndex;
  entity.value = event.params.value;
  entity.from = event.params.fromAddress;
  entity.to = event.params.toAddress;
  entity.save();
}
