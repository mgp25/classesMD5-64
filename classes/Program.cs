using System;
using System.IO;
using Ionic.Zip;
using System.Security.Cryptography;
using System.Text;


namespace classes
{
	class MainClass
	{
		static Ionic.Zip.ZipFile zip;
		static ZipEntry e;
		static byte[] hash;
		public static void Main (string[] args)
		{
			try
			{
				zip = Ionic.Zip.ZipFile.Read (args[0]);
			}
			catch(Exception z) 
			{
				Console.WriteLine ("File doesn't exist");
				Environment.Exit (0);
			}
			try
			{
				e = zip["classes.dex"];
			}
			catch(Exception z)
			{
				Console.WriteLine ("File inside .zip doesn't exist");
				Environment.Exit (0);
			}
			e.Extract (ExtractExistingFileAction.OverwriteSilently);

			var stream = new FileStream ("classes.dex", FileMode.Open,
				             FileAccess.Read,
				             FileShare.Read,
				             4096,
				             FileOptions.SequentialScan);

			var md5 = MD5.Create ();
			hash = md5.ComputeHash(stream);
			string base64hash = Convert.ToBase64String(hash);

			Console.WriteLine ("ClassesMD5: " + base64hash);
		}
	}
}