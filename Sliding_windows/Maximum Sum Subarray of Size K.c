

void subArraySum(int arr[], int k){
   
    int sum=0;

    for (int i=0;i<k;i++){
        sum+=arr[i]
    }
    
    int tempSum=sum;
    int w=0;
    for(int j=1; j<=n-k;j++){
         tempSum= tempSum-arr[w]+arr[w+k]
         w++;

         if(tempSum>sum){
            sum=tempSum
         }
    }
  

    return sum

}
    
