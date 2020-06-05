function sortNumber(a, b) {
    return a - b;
  }
  
  function getSecondLargest(nums) {
      // Complete the function
      nums.sort(sortNumber).reverse()
      let unique = [...new Set(nums)];
      let iterator1 = unique.values();
      let first = iterator1.next().value;
      let second = iterator1.next().value;
      return second;
  }