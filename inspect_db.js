// inspect_db.js
require('dotenv').config();
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_TOKEN });
const databaseId = process.env.NOTION_DB_ID;

(async () => {
    try {
        const db = await notion.databases.retrieve({ database_id: databaseId });

        console.log('✅ 資料庫名稱：', db.title[0]?.text?.content || '(未命名)');
        console.log('📌 欄位結構如下：\n');

        for (const [fieldName, fieldData] of Object.entries(db.properties)) {
            console.log(`🔸 ${fieldName}：${fieldData.type}`);
        }
    } catch (error) {
        console.error('❌ 取得欄位結構失敗：', error.message);
        if (error.body) {
            console.error(JSON.parse(error.body));
        }
    }
})();
