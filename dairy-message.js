const Discord = require('discord.js');
const client = new Discord.Client();
const cron = require('node-cron');

client.login('โทเคน');

// Schedule a message to be sent at 8:30 AM every day
cron.schedule('30 8 * * *', () => {
  client.channels.cache.get('YOUR_CHANNEL_ID').send('หวานใจมาบอกอรุณสวัสดิ์ค่ะ วันนี้ก็สู้ๆนะคะ!')
});
