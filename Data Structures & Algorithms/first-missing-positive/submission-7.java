class Solution {
    public int firstMissingPositive(int[] nums) {
        int l= nums.length;
        int max=-1;
        int min=1000000;
        for (int i=0; i<l; i++){
            if (nums[i]>=0 && nums[i]>max){
                max= nums[i];
            }
            if (nums[i]>=0 && nums[i]<min){
                min=nums[i];
            }
        }
        if (min>1){
            return 1;
        }
        int initmax=max;
        int maxfrommax=min;
        int minfrommin=max;
        int i=0;
        int t1=0;
        int t2=0;
        int m=0;
        int o=0;
        int e=0;
        while (true){ 
            o=0;
            if (nums[i]<=min || nums[i]>=max){
                o=1;
                    if (i<l-1){
                        i++;
                        System.out.println();
                        continue;
                    }
                    else {
                        e=1;
                        if (m==-1){
                            return initmax+1;
                        }
                        if (m==0){
                            m=-1;
                        }
                    }
            }
            if (o==0 && nums[i]>0 && nums[i]>maxfrommax){
                maxfrommax=nums[i];
                m=1;
            }
            if (o==0 && nums[i]>0 && nums[i]<minfrommin){
                minfrommin=nums[i];
                m=1;
            }
            if (i==l-1 && minfrommin==t2 && maxfrommax==t1){
                return initmax+1;
            }
            if (i==l-1 && minfrommin!=min+1){
                return min+1;
            }
            i++;
            if ((e==1 || i==l) && minfrommin!=maxfrommax){
                t1=min;
                t2= max;
                min= minfrommin;
                max= maxfrommax;
                minfrommin=t2;
                maxfrommax=t1;
                i=0;
                if (m==-1){
                    m=-1;
                }
                else{
                    m=0;
                }
                e=0;
            }
            if ((e==1 || i==l) && minfrommin == maxfrommax && maxfrommax+1==max){
                return initmax+1;
            }
            if ((e==1 || i==l) && minfrommin==maxfrommax && maxfrommax+1!=max){
                return maxfrommax+1;
            }
            System.out.println();
        }
    }
}