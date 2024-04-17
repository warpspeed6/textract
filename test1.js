function getReadyForBed() {
  let teethPromise = brushTeeth();
  let tempPromise = getRoomTemperature();

  // Change clothes based on room temperature
  return Promise.resolve(tempPromise)
    .then(temp => {
      // Assume `changeClothes` also returns a Promise
      if (temp > 20) {
        return Promise.resolve(changeClothes("warm"));
      } else {
        return Promise.resolve(changeClothes("cold"));
      }
    })
    .then(teethPromise)
    .then(Promise.resolve()); // since the async function returns nothing, ensure it's a resolved promise for `undefined`, unless it's previously rejected
}
