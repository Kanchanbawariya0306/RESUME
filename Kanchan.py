k = open("Kanchan.html","w")
a = """<html>
 <head>
<title>RESUME</title>
<style type="text/css">
    table {
        font-size: 18px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body>
<div >
  <center><h1><u>MY RESUME</u></h1></center>  
<h3> Kanchan Bawariya</h3>
<p > preetibwr03@gmail.com</p>
<p>DOB: 03 June 2000</p>
<p>Narayan Nagar Bhopal</p
<p>Contact No.: 7389030668</p>
 
  <h2><u>CAREER OBJECTIVE</u></h2>
  <p>To succeed in an environment of growth 
     and excellence in computer science and 
     earn a job which provide me job satisfaction
     and self development and help me in achieving
      personal as well as organization goals.</p>
            <h2><u>EDUCATION </u></h2>
            <table border="1">
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Flower Vale Higher Secondary School Jhurrey</td>
                    <td>79.5%</td>
                    <td>2015</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td>Govt. Kanya Shiksha Parisar Higher Secondary<br> School Chhindwara</td>
                    <td>67.4%</td>
                    <td>2017</td>
                </tr>
                <tr>
                    <td>1st Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>7.52 SGPA</td>
                    <td>2019</td>
                </tr>
                <tr>
                    <td>2nd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>7.58 SGPA</td>
                    <td>2019</td>
                </tr> 
                <tr>
                    <td>3rd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>8.04 SGPA</td>
                    <td>2020</td>
                </tr>
                
                
            </table>
        </div>
         <h2><u>HOBBIES</u></h2>
          <p>Reading books,Travelling</p>
           <p>Singing and Sketching</p>
          <h2><u>LANGUAGES</u></h2>
           <p>Hindi</p>
           <p>English.</p> 
          <h2><u>SKILLS</u></h2>
           <p>C,C++ and HTML.</p>
         <h2><u>WORK  EXPERIENCE</u></h2>
        <p>Fresher.</p>
</body>
</html>"""
k.write(a)
k.close()