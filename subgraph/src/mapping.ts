import {
  PunkBidEntered as PunkBidEnteredEvent,
  PunkBought as PunkBoughtEvent,
} from "../generated/Contract/Contract";
import { PunkBid, PunkBuy } from "../generated/schema";

export function handlePunkBidEntered(event: PunkBidEnteredEvent): void {
  let id = event.transaction.hash.toHex()
  let entity = new PunkBid(id);
  entity.index = event.params.punkIndex;
  entity.value = event.params.value;
  entity.from = event.params.fromAddress;
  entity.save();
}

export function handlePunkBought(event: PunkBoughtEvent): void {
  let id = event.transaction.hash.toHex()
  let entity = new PunkBuy(id);
  entity.index = event.params.punkIndex;
  entity.value = event.params.value;
  entity.from = event.params.fromAddress;
  entity.to = event.params.toAddress;
  entity.save();
}
