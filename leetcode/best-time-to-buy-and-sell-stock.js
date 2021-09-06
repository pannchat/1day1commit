var maxProfit = function(prices) {
    //     while(prices.length){
    //        const a = prices.shift();
    //         if(Math.max(...prices) > a) 
    //             Math.max(...prices)-a > tmp 
    //                 ? tmp=Math.max(...prices)-a
    //                 : null
    
    //     }
        let min = prices[0];
        let valDiff = 0;
        for(let i =1; i<prices.length; i++){
            if (prices[i] < min)
                min = prices[i];
            else{
                let diff = prices[i] - min;
                valDiff < diff ? valDiff=diff : null;
            }
        }
        return valDiff
    };