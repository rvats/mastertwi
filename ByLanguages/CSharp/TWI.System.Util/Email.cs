using System.IO;
using System.Net;
using System.Net.Mail;
using System.Net.Mime;


namespace TWI.System.Util
{
    class Email
    {
        public Email()
        {
            MailMessage m = new MailMessage();
            SmtpClient sc = new SmtpClient();

            m.From = new MailAddress("vats.rahul@gmail.com", "Rahul Vats");
            m.To.Add(new MailAddress("arpitavats1987@gmail.com", "Arpita Vats"));
            m.CC.Add(new MailAddress("errahulvats@gmail.com", "Rahul Vats"));
            m.Bcc.Add(new MailAddress("vats.rahul@gmail.com", "Rahul Vats"));
            //similarly BCC
            m.Subject = "Test";
            m.Body = "This is a Test Mail";

            FileStream fs = new FileStream("D:\\Test\\MSJAR_Vol1.pdf", FileMode.Open, FileAccess.Read);
            Attachment a = new Attachment(fs, "MSJAR_Vol1.pdf", MediaTypeNames.Application.Octet);
            m.Attachments.Add(a);

            string str = "<html><body><h1>Picture</h1><br/><img src=\"cid:image1\"></body></html>";
            AlternateView av = AlternateView.CreateAlternateViewFromString(str, null, MediaTypeNames.Text.Html);
            LinkedResource lr = new LinkedResource("D:\\Test\\hello.jpg", MediaTypeNames.Image.Jpeg);
            lr.ContentId = "image1";
            av.LinkedResources.Add(lr);
            m.AlternateViews.Add(av);

            sc.Host = "smtp.gmail.com";
            sc.Port = 587;
            sc.Credentials = new NetworkCredential("vats.rahul@gmail.com", "**************");
            sc.EnableSsl = true; // runtime encrypt the SMTP communications using SSL
            sc.Send(m);
        }
    }
}
