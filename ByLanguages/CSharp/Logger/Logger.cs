using System;

namespace Logger
{
    public static class Logger
    {
        private static readonly NLog.Logger logger = NLog.LogManager.GetCurrentClassLogger();

        public static void Log(Exception ex)
        {
            logger.Error(ex);
        }
    }
}
