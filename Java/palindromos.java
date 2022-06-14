public class palindromos {
    public static void main(String[] args) {
        String s="aba";
        char [] s_char = s.toLowerCase().toCharArray();
        String inv="";

        for(int i=s_char.length-1; i>-1; i--){
            inv = inv+s_char[i];
        }
        if( inv.toLowerCase().equals(s.toLowerCase() ) ){
            System.out.println("Es un palindromo");
        }
        else{
            System.out.println("No es un palindromo");
        }
    }
}

