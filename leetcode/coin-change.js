var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity); 
    // amount + 1의 길이를 가지는 배열을 만든 후 0으로 채운다.
    dp[0] = 0; 
  
  
      for(let i = 1; i<dp.length; i++){
          for(const coin of coins){
          console.log(i,coin)
          if((i-coin)>=0){
              dp[i]=Math.min(dp[i], dp[i-coin]+1)
          }
      }
  }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
  
  };
  