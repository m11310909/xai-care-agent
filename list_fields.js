// list_fields.js

require('dotenv').config();
const { Client } = require('@notionhq/client');

// 初始化 Notion 客戶端
const notion = new Client({ auth: process.env.NOTION_TOKEN });

async function listDatabaseFields() {
    const databaseId = process.env.NOTION_DB_ID;

    try {
        const response = await notion.databases.retrieve({ database_id: databaseId });

        console.log(`🔎 資料庫名稱：${response.title[0].text.content}`);
        console.log('📋 欄位結構如下：');

        const props = response.properties;
        for (const [name, prop] of Object.entries(props)) {
        }
    } catch (error) {
        console.error('❌ 無法讀取資料庫欄位，請檢查 NOTION_TOKEN 與 NOTION_DB_ID 是否正確。');
        if (error.body) {
            console.error(JSON.parse(error.body));
        } else {
            console.error(error);
        }
    }
}

listDatabaseFields();
