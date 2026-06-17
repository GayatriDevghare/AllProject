import java.awt.*;
import java.awt.event.*;
class MyFrame extends Frame implements ActionListener
{
    TextField t1,t2;
    Button b1,b2,b3,b4;
    TextArea txt;
    public MyFrame()
    {
        setLayout(new FlowLayout());
        t1=new TextField(10);
        t2=new TextField(10);
        b1=new Button("+");
        b2=new Button("-");
        b3=new Button("*");
        b4=new Button("/");
        txt=new TextArea(5,20);
        add(txt); add(t1); add(t2);
        add(b1); b1.addActionListener(this);
        add(b2); b2.addActionListener(this);
        add(b3); b3.addActionListener(this);
        add(b4); b4.addActionListener(this);
    }
    public void actionPerformed(ActionEvent e)
    {
        double n1=Double.parseDouble(t1.getText());
        double n2=Double.parseDouble(t2.getText());
        double cmd; String cmd=g.getActionCommand();
        if(cmd.equals("+"))n=n1+n2;
        if(cmd.equals("-"))n=n1-n2;
        if(cmd.equals("*"))n=n1*n2;
        if(cmd.equals("/"))n=n1/n2;
        String num=String.valueOf(n);
        String exp=num1+" "+cmd+" "+num2+" "+num;
        txt.insert(exp+"\n",0);
    }

}
class demo
{
    public static void main(String[] args)
    {
        MyFrame frm=new MyFrame();
        frm.setTitle("CCIT");
        frm.setSize(200,200);
        frm.setVisible(true);
        
    }
}