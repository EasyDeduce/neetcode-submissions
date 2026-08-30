class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphaNumeric(char){
        return /^[a-zA-Z0-9]$/.test(char)
    }
    isPalindrome(s) {
        s=s.toLowerCase();
        let a='a';
        let z='z';
        let temp="";
        for (let i=0; i<s.length; i++){
            if (this.isAlphaNumeric(s[i])){
                temp=temp+s[i];
            }
        }
        s=temp;
        console.log(s);
        for (let i=0;i<(s.length/2); i++){
            if (s[i]!=s[s.length-i-1]){
                return false;
            }
        }
        return true
    }
}
