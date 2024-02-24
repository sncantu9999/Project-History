import java.sql.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

import com.mysql.cj.log.Log;
import com.mysql.cj.x.protobuf.MysqlxCrud.Find;

import java.io.*;
import java.lang.module.FindException;
import java.util.*;
import java.net.*;
import java.util.ArrayList;

import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;    

class GlobalHolder {
    public Connection conn;
    public String userName;
    public boolean buttonPressed;
    public boolean LoggedIn;
    public String password;
    public String message;
    public String name;
    public String age;
    public String grade;
    public String id;
    public String courseGrade;
    public String course;
    public String year;
    public String orgcourse;
    public String newcourseGrade;
    public String deleteclassName;


    void addConn(Connection con) {conn = con;}
    void addUserName(String user) {userName = user;}
    void addbuttonPressed(boolean press) {buttonPressed = press;}
    void addLoggedIn(boolean login) {LoggedIn = login;}
    void addPassword(String pass) {password = pass;}
    void addMessage(String mes) {message = mes;}
    void addname(String student) {name = student;}
    void addage(String studentage) {age = studentage;}
    void addgrade(String studentgrade) {grade = studentgrade;}
    void addid(String studentid) {id = studentid;}
    void addcourse(String studentid) {course = studentid;}
    void addcourseGrade(String studentid) {courseGrade = studentid;}
    void addyear(String studentid) {year = studentid;}
    void addorgcourse(String studentid) {orgcourse = studentid;}
    void addnewcourseGrade(String studentid) {newcourseGrade = studentid;}
    void deleteclassName(String studentid) {deleteclassName = studentid;}
}

public class App {

    /**
     * @param args the command line arguments
     */
    public static void ShowLogin(GlobalHolder gh) {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");  
            String url="jdbc:mysql://localhost:3306/javachat";
            String username="root";
            String password="";//your password
            Connection conn = DriverManager.getConnection(url,username,password);
            gh.addConn(conn);
            Statement s = gh.conn.createStatement();            
            JFrame jf = new JFrame("Grading System");
            jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            JPanel newPanel = new JPanel();
            newPanel.setLayout(new GridLayout(7,1));
            JLabel label = new JLabel("Enter Username: (Press Enter to confirm)");
            JTextField userName = new JTextField(20);
            userName.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    gh.addUserName(userName.getText());
                }
            });
            newPanel.add(label);
            newPanel.add(userName);
            JLabel labelPassword = new JLabel("Enter password: (Press Enter to confirm)");
            JPasswordField fieldPassword = new JPasswordField(20);
            fieldPassword.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    gh.addPassword(new String(fieldPassword.getPassword()));
                }
            });
            JButton buttonLogin = new JButton("Login");
            newPanel.add(labelPassword);
            newPanel.add(fieldPassword);
            newPanel.add(buttonLogin);
            jf.add(newPanel);
            jf.setSize(1000,400);
            jf.setVisible(true);
            buttonLogin.addActionListener(new ButtonPressed(gh, jf, conn, s));
            newPanel.add(buttonLogin);
        } catch(Exception e){  
            System.out.println("Caught exception: "+e.toString());
        }
    }
    public static void main(String[] args){
        GlobalHolder gh = new GlobalHolder();
        ShowLogin(gh);
    }
}
    class ButtonPressed implements ActionListener{

        Statement statement;
        JFrame jf;
        Connection conn;
        GlobalHolder glh;

        ButtonPressed(GlobalHolder gh, JFrame jframe, Connection cn, Statement s) {
            glh = gh;
            gh.buttonPressed = true;
            statement = s;
            jf = jframe;
            conn = cn;
        }
        @Override
        public void actionPerformed(ActionEvent e) {
            String query = "SELECT * FROM User WHERE username = '"+ glh.userName +"' AND pass = '"+ glh.password +"'";
            try{
            ResultSet rs= statement.executeQuery(query);
            if (rs.next()) {
                glh.LoggedIn = true;
                jf.setVisible(false);
                new SecondScreen(glh, statement);
            }
            else{
                PopupFactory pf = new PopupFactory();
                JLabel l = new JLabel("Incorrect Login");
                JPanel p2 = new JPanel();
                p2.setBackground(Color.red);
                p2.add(l);
                // create a popup
                Popup p = pf.getPopup(jf, p2, 180, 100);
                p.show();
            }
        }
        catch(SQLException sqle) {System.out.println(sqle);}
        }
}

class SecondScreen {
    SecondScreen(GlobalHolder glh, Statement statement) {
        JFrame jf2 = new JFrame("Choose Student");
        jf2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel newPan = new JPanel();
        newPan.setLayout(new GridLayout(13,1));
        JLabel header = new JLabel("Add a Student:");
        JLabel labelnewStudent = new JLabel("Add Student Name:");
            JTextField Newname = new JTextField(50);
            Newname.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    glh.addname(Newname.getText());
                }
            });
        JLabel labelnewStudentAge = new JLabel("Add Student Age:");
        JTextField newage = new JTextField(50);
        newage.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                glh.addage(newage.getText());
            }
        });
        JLabel labelnewStudentGrade = new JLabel("Add Student School Year (ex. Freshman)");
        JTextField newgrade = new JTextField(50);
        newgrade.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                glh.addgrade(newgrade.getText());
            }
        });
        JButton buttonLogin = new JButton("Add");
        buttonLogin.addActionListener(new AddStudentPressed(glh, jf2, statement));
        newPan.add(header);
        newPan.add(labelnewStudent);
        newPan.add(Newname);
        newPan.add(labelnewStudentAge);
        newPan.add(newage);
        newPan.add(labelnewStudentGrade);
        newPan.add(newgrade);
        newPan.add(buttonLogin);
        newPan.add(new JLabel());
        newPan.add(new JLabel("Find a Student:"));
        JLabel labelGetStudent = new JLabel("Enter Student's ID:");
            JTextField studentID = new JTextField(50);
            studentID.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    glh.addid(studentID.getText());
                }
            });
        newPan.add(labelGetStudent);
        newPan.add(studentID);
        JButton FindButton = new JButton("Find");
        FindButton.addActionListener(new FindStudent(glh, jf2, statement));
        newPan.add(FindButton);
        jf2.setSize(1000,400);
        jf2.setVisible(true);
        jf2.add(newPan);
    }
}

class AddStudentPressed implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    AddStudentPressed(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        int randomNumber = 0;
        Random rand = new Random();
        for(int i = 0; i < 5; i++) {
            randomNumber += rand.nextInt();
        }
        if(randomNumber < 0) {randomNumber = randomNumber*-1;}
        System.out.println(randomNumber);
        glh.addid(""+randomNumber);
        String query = "Insert into students values("+ randomNumber +",'"+ glh.name +"','"+ glh.age +"','"+ glh.grade +"')";
        try{
        int rows= statement.executeUpdate(query);
        if (rows != 0) {
            jf.setVisible(false);
            new ThirdScreen(glh, statement);
        }
        else{
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Student could not be added");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.red);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
    }
    catch(SQLException sqle) {System.out.println(sqle);}
}}

class FindStudent implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    FindStudent(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        String query = "Select * from students where ID = '"+ glh.id + "'";
        try{
            ResultSet rs = statement.executeQuery(query);
        if (rs.next()) {
            jf.setVisible(false);
            new ThirdScreen(glh, statement);
        }
        else{
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Student could not be found");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.red);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
    }
    catch(SQLException sqle) {System.out.println(sqle);}
}}

class ThirdScreen {

    ThirdScreen(GlobalHolder glh, Statement statement) {
        JFrame jf2 = new JFrame("Student Information");
        jf2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel newPan = new JPanel();
        newPan.setLayout(new GridLayout(25,1));
        JButton buttonLogin = new JButton("Upload transcript");
        buttonLogin.addActionListener(new UploadButton(glh, jf2, statement));
        JLabel header = new JLabel("Add Student Course:");
        JLabel labelcourse = new JLabel("Enter Course Name:");
            JTextField course = new JTextField(50);
            course.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    glh.addcourse(course.getText());
                }
            });
        JLabel labelgrade = new JLabel("Enter Student Grade:");
        JTextField newgrade = new JTextField(50);
        newgrade.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                glh.addcourseGrade(newgrade.getText());
            }
        });
        JLabel labelyear = new JLabel("Enter Student Year:");
        JTextField newyear = new JTextField(50);
        newyear.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                glh.addyear(newyear.getText());
            }
        });
        JButton addButton = new JButton("Add");
        addButton.addActionListener(new AddCourseButton(glh, jf2, statement));
        JLabel header2 = new JLabel("Edit Student Grade:");
        JLabel orgcourselabel = new JLabel("Enter Course Name:");
            JTextField orgcourse = new JTextField(50);
            orgcourse.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    glh.addorgcourse(orgcourse.getText());
                }
            });
        JLabel labelnewgrade = new JLabel("Enter New Grade:");
        JTextField newgrade2 = new JTextField(50);
        newgrade2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                glh.addnewcourseGrade(newgrade2.getText());
            }
        });
        JButton updateButton = new JButton("Update");
        updateButton.addActionListener(new UpdateButton(glh, jf2, statement));
        JLabel header3 = new JLabel("Delete Student Course:");
        JLabel deletecourselabel = new JLabel("Enter Course Name:");
            JTextField deletecourse = new JTextField(50);
            deletecourse.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    glh.deleteclassName(deletecourse.getText());
                }
            });
        JButton deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new DeleteCourseButton(glh, jf2, statement));
        newPan.add(new JPanel());
        newPan.add(buttonLogin);
        newPan.add(new JPanel());
        newPan.add(header);
        newPan.add(labelcourse);
        newPan.add(course);
        newPan.add(labelgrade);
        newPan.add(newgrade);
        newPan.add(labelyear);
        newPan.add(newyear);
        newPan.add(addButton);
        newPan.add(new JPanel());
        newPan.add(header2);
        newPan.add(orgcourselabel);
        newPan.add(orgcourse);
        newPan.add(labelnewgrade);
        newPan.add(newgrade2);
        newPan.add(updateButton);
        newPan.add(new JPanel());
        newPan.add(header3);
        newPan.add(deletecourselabel);
        newPan.add(deletecourse);
        newPan.add(deleteButton);
        JButton graphButton = new JButton("View Bar Graph Breakdown");
        graphButton.addActionListener(new Graph(glh, jf2, statement));
        newPan.add(new JPanel());
        newPan.add(graphButton);
        jf2.setSize(1400,800);
        jf2.setVisible(true);
        jf2.add(newPan);
    }
}

class Graph implements ActionListener {
    GlobalHolder glh;
    JFrame jf;
    Statement statement;

    Color getRandomColor() {
        Random rand = new Random();
        float r = rand.nextFloat();
        float g = rand.nextFloat();
        float b = rand.nextFloat();
        return new Color(r, g, b);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String title = "GPA Breakdown";
        CalculateGPA calc = new CalculateGPA(glh, statement);
        boolean hasGrades = false;
        if(calc.hasGrades()) {hasGrades = true;}
        HashMap<String, Float> yearGPAs = calc.getGPAs();
        ArrayList<String> labels = new ArrayList<String>();
        ArrayList<Float> values = new ArrayList<Float>();
        ArrayList<Color> colors = new ArrayList<Color>();
        for(String year : yearGPAs.keySet()) {
            labels.add(year);
        }
        for(Float GPA : yearGPAs.values()) {
            values.add(GPA);
        }
        for(String i : labels) {
            colors.add(getRandomColor());
        }
        BarChart bc = new BarChart(values, labels, colors, title);
        jf.setVisible(false);
        JFrame jf2 = new JFrame("Bar Graph");
        jf2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        if(hasGrades) {
        jf2.add(new JLabel("Grade Breakdown"));
        jf2.add(bc);
        }
        else{
            jf2.add(new JLabel("Student has no grades to show"));
        }
        jf2.setSize(1400,800);
        jf2.setVisible(true);
    }

    public Graph(GlobalHolder glh, JFrame jf, Statement statement){
        this.glh = glh;
        this.jf = jf;
        this.statement = statement;
    }
}
class BarChart extends JPanel {
    ArrayList<String> labels = new ArrayList<String>();
    ArrayList<Float> values = new ArrayList<Float>();
    ArrayList<Color> colors = new ArrayList<Color>();
    private String title;
 
  public BarChart(ArrayList<Float> values, ArrayList<String> labels, ArrayList<Color> colors, String title) {
    this.labels = labels;
    this.values = values;
    this.colors = colors;
    this.title = title;
  }
 
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    if (values == null || values.size() == 0) {
      return;
    }
 
    double minValue = 0;
    double maxValue = 0;
    for (int i = 0; i < values.size(); i++) {
      if (minValue > values.get(i)) {
        minValue = values.get(i);
      }
      if (maxValue < values.get(i)) {
        maxValue = values.get(i);
      }
    }

    Dimension dimension = getSize();
    int widthPanel = dimension.width;
    int heightPanel = dimension.height;
    int widthBar = widthPanel / values.size();
 
    Font labelFont = new Font("Roboto", Font.PLAIN, 14);
    FontMetrics labelMetrics = g.getFontMetrics(labelFont);

    Font titleFont = new Font("Roboto", Font.BOLD, 15);
    FontMetrics titleMetrics = g.getFontMetrics(titleFont);
    g.setFont(titleFont);

    int widthTitle = titleMetrics.stringWidth(title);
    int heightString = titleMetrics.getAscent();
    int widthString = (widthPanel - widthTitle) / 2;
    g.drawString(title, widthString, heightString);
 
    int top = titleMetrics.getHeight();
    int bottom = labelMetrics.getHeight();
    if (maxValue == minValue) {
      return;
    }
    double scale = (heightPanel - top - bottom) / (maxValue - minValue);
    heightString = heightPanel - labelMetrics.getDescent();
    g.setFont(labelFont);
    for (int j = 0; j < values.size(); j++) {
      int value = j * widthBar + 1;
      int valuetop = top;
      double heightdouble = (values.get(j) * scale);
      int height = (int)heightdouble;
      
      if (values.get(j) >= 0) {
        valuetop += (int) ((maxValue - values.get(j)) * scale);
      } else {
        valuetop += (int) (maxValue * scale);
        height = -height;
      }
 
      g.setColor(colors.get(j));
      g.fillRect(value, valuetop, widthBar - 2, height);
      g.setColor(Color.black);
      g.drawRect(value, valuetop, widthBar - 2, height);
 
      int labelWidth = labelMetrics.stringWidth(labels.get(j));
      widthString = j * widthBar + (widthBar - labelWidth) / 2;
      g.drawString(labels.get(j), widthString, heightString);
    }
  }
}

class CalculateGPA {
    Statement statement;
    GlobalHolder glh;
    ArrayList<String> years = new ArrayList<String>();
    HashMap<String, Float> yearGPAs = new HashMap<String, Float>();
    boolean hasGrades = false;

    public CalculateGPA(GlobalHolder g, Statement s) {
        statement = s;
        glh = g;
        String query = "Select * from takes where studentID = '"+ glh.id + "'";
        try{
            ResultSet rs = statement.executeQuery(query);
        while (rs.next()) {
            hasGrades = true;
            String year = rs.getString(3);
            if(!years.contains(year)) {years.add(year);}
        }
        }
        catch(SQLException sqle) {System.out.println(sqle);}
        for(String year : years) {
            Float yearGPA = 0.0f;
            Float yearGPAAvg = 0.0f;
            Float numRows = 0f;
            String query2 = "Select grade from takes where studentID = '"+ glh.id + "' and year = '"+ year +"'";
            try{
                ResultSet rs = statement.executeQuery(query2);
            while (rs.next()) {
                numRows++;
                String grade = rs.getString(1);
                yearGPA += letterToNumberGrade(grade);
            }
            yearGPAAvg = yearGPA / numRows;
            yearGPAs.put(year+" ("+yearGPAAvg+")", yearGPAAvg);
            }
            catch(SQLException sqle) {System.out.println(sqle);}
        }
    }

    HashMap<String, Float> getGPAs() {return yearGPAs;}

    boolean hasGrades() {return hasGrades;}

    Float letterToNumberGrade(String grade) {
        Float numberGrade = 0f;
        switch(grade) {
            case "A":
                numberGrade = 4.00f;
                break;
            case "A-":
                numberGrade = 3.7f;
                break;
            case "B+":
                numberGrade = 3.3f;
                break;
            case "B":
                numberGrade = 3.0f;
                break;
            case "B-":
                numberGrade = 2.7f;
                break;
            case "C+":
                numberGrade = 2.3f;
                break;
            case "C":
                numberGrade = 2.0f;
                break;
            case "C-":
                numberGrade = 1.7f;
                break;
            case "D+":
                numberGrade = 1.3f;
                break;
            case "D":
                numberGrade = 1.0f;
                break;
            case "F":
                numberGrade = 0.0f;
                break;
        }
        return numberGrade;
    }
}

class UploadButton implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    UploadButton(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        JFileChooser file_upload = new JFileChooser();
        file_upload.setCurrentDirectory(new File("."));
        int res = file_upload.showOpenDialog(null);
        if(res == JFileChooser.APPROVE_OPTION) {
            File selectedFile = file_upload.getSelectedFile();
            ArrayList<String> lines = new ArrayList<String>();
            try (Scanner scanner = new Scanner(selectedFile)) {
                int ignoreLines = 1;
                while (scanner.hasNextLine()) {
                    String line = scanner.nextLine();
                    if(ignoreLines > 3) {
                        if (!line.isEmpty()) {
                            lines.add(line);
                        }
                    }
                    ignoreLines += 1;
                }
            }
            catch (FileNotFoundException ex) {
                ex.printStackTrace();
            }
            for(int i = 0; i < lines.size(); ++i){
                String line = lines.get(i);
                System.out.println(line);
                String[] arrOfStr = line.split("\t");
                System.out.println(arrOfStr.length);
                System.out.println("First"+arrOfStr[0]);
                System.out.println("Second"+arrOfStr[1]);
                System.out.println("Third"+arrOfStr[2]);
                String query = "Insert into takes values('"+ arrOfStr[1] +"','"+ glh.id +"','"+ arrOfStr[0] +"','"+ arrOfStr[2]+"')";
                try{
                int rows= statement.executeUpdate(query);
                if (rows != 0) {
                    PopupFactory pf = new PopupFactory();
                    JLabel l = new JLabel("Successfully updated");
                    JPanel p2 = new JPanel();
                    p2.setBackground(Color.green);
                    p2.add(l);
                    // create a popup
                    Popup p = pf.getPopup(jf, p2, 180, 100);
                    p.show();
                }
                else{
                    PopupFactory pf = new PopupFactory();
                    JLabel l = new JLabel("File could not be read.");
                    JPanel p2 = new JPanel();
                    p2.setBackground(Color.red);
                    p2.add(l);
                    // create a popup
                    Popup p = pf.getPopup(jf, p2, 180, 100);
                    p.show();
                }
            }
            catch(SQLException sqle) {System.out.println(sqle);}
        }
        }
}
}

class UpdateButton implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    UpdateButton(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println(glh.course);
        System.out.println(glh.courseGrade);
        System.out.println(glh.id);
        String query = "update takes set grade = '"+ glh.newcourseGrade + "' where studentID = '"+ glh.id + "' and classname = '"+ glh.orgcourse+ "'";
        try{
           int rows = statement.executeUpdate(query);
            if (rows != 0) {
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Grade Changed!");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.green);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
        else{
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Grade could not be changed");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.red);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
    }
    catch(SQLException sqle) {System.out.println(sqle);}
}
}
class AddCourseButton implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    AddCourseButton(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println(glh.courseGrade);
        String query = "Insert into takes values('"+ glh.course +"','"+ glh.id +"','"+ glh.year +"','"+ glh.courseGrade +"')";
        try{
           int rows = statement.executeUpdate(query);
            if (rows != 0) {
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Course was added");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.green);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
        else{
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Course could not be added");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.red);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
    }
    catch(SQLException sqle) {System.out.println(sqle);}
}
}

class DeleteCourseButton implements ActionListener{

    Statement statement;
    JFrame jf;
    GlobalHolder glh;

    DeleteCourseButton(GlobalHolder gh, JFrame jfr, Statement s) {
        glh = gh;
        statement = s;
        jf = jfr;
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println(glh.courseGrade);
        String query = "delete from takes where studentID = '"+ glh.id +"' and classname = '"+ glh.deleteclassName+"'";
        try{
           int rows = statement.executeUpdate(query);
            if (rows != 0) {
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Course was deleted");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.green);
            p2.add(l);
            // create a popup
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
        else{
            PopupFactory pf = new PopupFactory();
            JLabel l = new JLabel("Course could not be deleted");
            JPanel p2 = new JPanel();
            p2.setBackground(Color.red);
            p2.add(l);
            Popup p = pf.getPopup(jf, p2, 180, 100);
            p.show();
        }
    }
    catch(SQLException sqle) {System.out.println(sqle);}
}
}