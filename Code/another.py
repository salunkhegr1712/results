

# Example usage
if __name__ == "__main__":
    # HTML content to convert to image
    html_content = """
      <table align="center" bgcolor="#FFFF99" border="0" cellpadding="0" cellspacing="0" width="91%">
      <tr>
      <td bgcolor="#FFFFFF" width="34%">
      <p align="center"><b><font color="#FF0000" size="4">MAHARASHTRA UNIVERSITY OF HEALTH SCIENCES, NASHIK</font></b> </p>
      <p align="center"><b><font color="#6600CC">STATEMENT OF MARKS FOR <font color="#0000CC">THIRD (II) MBBS - (2019) - Winter-2023</font></font></b></p>
      <p align="center"><strong>Name of the Student</strong>:- RODGE ARCHANA MAHADEV</p>
      <p align="center"><span class="style2">College:- </span>Grant Government Medical College,Mumbai</p>
      <p align="center"><span class="style2">Seat No:-</span>212127    <span class="style2"> PRN No:-</span> AAB0120190033</p>
      </td>
      </tr>
      </table>
      <table align="center" bgcolor="#CCFFCC" border="1" bordercolor="#000000" width="61%">
      <tr>
      <td bgcolor="#FFCCCC" rowspan="2" valign="top" width="27%"><div align="center"><font size="3">HEAD</font>S / <font size="3">SUBJECTS  </font></div></td>
      <td bgcolor="#FFCCCC" rowspan="2" valign="top" width="9%"><div align="center"><font size="3">THEORY <br/> TOTAL </font></div>
      <p align="center"> </p></td>
      <td bgcolor="#FFCCCC" rowspan="2" valign="top" width="5%"><p align="center"><font size="3">
            PRACTICAL+ORAL</font></p></td>
      <td bgcolor="#FFCCCC" rowspan="2" valign="top" width="8%"><div align="center"><font size="3">TOTAL <br/> THEORY+PRACT.</font></div></td>
      <td bgcolor="#FFCCCC" colspan="2" valign="top"><div align="center"><font size="3">INTERNAL ASSESSMENT</font></div></td>
      <td bgcolor="#FFCCCC" rowspan="2" valign="top" width="6%"><div align="center"><b><font size="3">TOTAL</font></b></div></td>
      </tr>
      <tr>
      <td bgcolor="#FFCCCC" height="23" valign="top" width="7%"><div align="center"><font size="3">THEORY</font></div></td>
      <td bgcolor="#FFCCCC" height="23" valign="top" width="7%"><div align="center"><font size="3">PRACT.</font></div></td>
      </tr>
      <tr bgcolor="#66FFCC">
      <td align="left"><div align="right"><strong>MAX</strong></div></td>
      <td><div align="center">200</div></td>
      <td><div align="center">200</div></td>
      <td height="26" valign="top"><div align="center">400</div></td>
      <td height="26" valign="top"><div align="center">50</div></td>
      <td height="26" valign="top"><div align="center">50</div></td>
      <td><div align="center"><strong>100</strong></div></td>
      </tr>
      <tr bgcolor="#66FFCC">
      <td align="left"><div align="right"><strong>MIN</strong></div></td>
      <td><div align="center">80</div></td>
      <td><div align="center">80</div></td>
      <td height="26" valign="top"><div align="center">200</div></td>
      <td height="26" valign="top"><div align="center">20</div></td>
      <td height="26" valign="top"><div align="center">20</div></td>
      <td><div align="center"><strong>50</strong></div></td>
      </tr>
      <tr>
      <td align="right"><font size="3">Gen.Medicine</font></td>
      <td width="9%"><div align="center"><font size="3">133</font></div></td>
      <td width="5%"><div align="center"><font size="3">102</font></div></td>
      <td height="26" valign="top" width="8%"><div align="center"><font size="3">235</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">33</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">30</font></div></td>
      <td width="6%"><div align="center"><b><font size="3">063</font></b></div></td>
      </tr>
      <tr>
      <td align="right"><font size="3">Gen. Surgery</font></td>
      <td width="9%"><div align="center"><font size="3">136</font></div></td>
      <td width="5%"><div align="center"><font size="3">159</font></div></td>
      <td height="26" valign="top" width="8%"><div align="center"><font size="3">295</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">31</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">38</font></div></td>
      <td width="6%"><div align="center"><b><font size="3">069</font></b></div></td>
      </tr>
      <tr>
      <td align="right"><font size="3">Obgy. &amp; Gynae.</font></td>
      <td width="9%"><div align="center"><font size="3">135</font></div></td>
      <td width="5%"><div align="center"><font size="3">158</font></div></td>
      <td height="26" valign="top" width="8%"><div align="center"><font size="3">293</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">34</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">32</font></div></td>
      <td width="6%"><div align="center"><b><font size="3">066</font></b></div></td>
      </tr>
      <tr bgcolor="#66FFCC">
      <td align="left"><div align="right"><strong>MAX</strong></div></td>
      <td><div align="center">100</div></td>
      <td><div align="center">100</div></td>
      <td height="26" valign="top"><div align="center">200</div></td>
      <td height="26" valign="top"><div align="center">25</div></td>
      <td height="26" valign="top"><div align="center">25</div></td>
      <td><div align="center"><strong>50</strong></div></td>
      </tr>
      <tr bgcolor="#66FFCC">
      <td align="left"><div align="right"><strong>MIN</strong></div></td>
      <td><div align="center">40</div></td>
      <td><div align="center">40</div></td>
      <td height="26" valign="top"><div align="center">100</div></td>
      <td height="26" valign="top"><div align="center">10</div></td>
      <td height="26" valign="top"><div align="center">10</div></td>
      <td><div align="center"><strong>25</strong></div></td>
      </tr>
      <tr>
      <td align="right"><font size="3">Paediatrics</font></td>
      <td width="9%"><div align="center"><font size="3">066</font></div></td>
      <td width="5%"><div align="center"><font size="3">065</font></div></td>
      <td height="26" valign="top" width="8%"><div align="center"><font size="3">131</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">14</font></div></td>
      <td height="26" valign="top" width="7%"><div align="center"><font size="3">15</font></div></td>
      <td width="6%"><div align="center"><b><font size="3">029</font></b></div></td>
      </tr>
      <tr>
      <td #66ffcc"="" bgcolor="#00FFCC" colspan="4"><div align="right"><b><font size="3">GRAND TOTAL : </font></b></div></td>
      <td bgcolor="#66FFCC" colspan="5"><div align="left">0954 <strong>/ 1400 </strong></div></td>
      </tr>
      <tr>
      <td bgcolor="#66FFCC" colspan="4"><div align="right"><b><font size="3">RESULT :</font></b></div></td>
      <td bgcolor="#66FFCC" colspan="5"><div align="left">PASS </div></td>
      </tr>
      <tr>
      <td bgcolor="#66FFCC" colspan="4"><div align="right"><b><font size="3">REMARK :</font></b></div></td>
      <td bgcolor="#66FFCC" colspan="5"><div align="left"></div></td>
      </tr>
      </table>
      <!-- <p><strong>Result Date</strong>:- <b><font size="3">28 March 2024</font></b></p> -->
      <p align="justify"><b><i><font size="3">NOTE:</font></i></b><font size="2"> 1) Internal assessment marks are not considered for Grand total.</font></p>
      <p align="justify"><b><i><font size="3"> 2) The above result is subject to change in case of any error in the processing of the results in accordance with the provisions under section-67 of Ordinance 1/2014.</font></i></b></p>
      <p align="justify"><b><i><font size="3"> 3) For Verification  of marks of Theory/Practical/Oral/Viva only (If any), send an application with prescribed fees through the college before <b><font size="3">04/04/2024 As per Circ.65/2022,03/10/22</font>.</b>  And for Photostate(Xerox) copies of Answer books (If any), send and Application with requisite fee through the college before <b><font size="3">04/04/2024 As per Circ.65/2022,03/10/22</font></b>. </font></i></b></p>
      <p>
      </p></body>
      </html>
    """

    # Output filename for the image
    output_filename = 'output_image.png'

    # Convert HTML to image
    html_to_image(html_content, output_filename)
