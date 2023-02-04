import java.util.*; 

class Test {
    public String hello(String name, int age) {
        return "Hello my name is " + name + " and I'm " + age + " years old";
    }

    public static void main(String[] args) {
        Test t = new Test();
        Set<Integer> s = new HashSet<>();
        s.add(1);
        s.add(2);
        s.add(1);
        System.out.println(s);
    	System.out.println(t.hello("Monica", 99));
    }
}
