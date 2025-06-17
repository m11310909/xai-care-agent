require('dotenv').config();
const { logCommitsToNotion } = require('notion-logger');

logCommitsToNotion();

const notionLogger = require('notion-logger');

notionLogger.log(); // 就會自動將最近 commit 寫入 Notion
