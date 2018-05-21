using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace VueJuniorDemo.Handler
{
    /// <summary>
    /// Handler1 的摘要说明
    /// </summary>
    public class Handler1 : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            string type = context.Request.Params["type"];
            if (type=="login")
            {
                DoLogin(context);
            }
        }

        public void DoLogin(HttpContext context) {
            string name = context.Request.Form["name"];
            string pwd = context.Request.Form["pwd"];
            if (new string(name.ToCharArray().Reverse().ToArray()) == pwd)
            {
                context.Response.ContentType = "text/plain";
                context.Response.Write("success");
            }
            else
            {
                context.Response.ContentType = "text/plain";
                context.Response.Write("fail");
            }
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }
}