import telebot
import yfinance as yf

TOKEN = "8658406238:AAHIm18xnpbe91uypHZfI6awCW5DF43QUY4"
CHAT_ID = "5496814596"

bot = telebot.TeleBot(TOKEN)

ativos = {
    "FWRA": "FWRA.L",
    "AVUV": "AVUV",
    "IWVL": "IWVL.L",
    "EMVL": "EMVL.L",
    "DÓLAR": "USDBRL=X"
}

mensagem = "📊 **Análise de ETFs (Média de 50 dias):**\n\n"

for nome, ticker in ativos.items():
    dados = yf.Ticker(ticker)
    historico = dados.history(period="3mo")
    preco_atual = historico['Close'].iloc[-1]
    media_50 = historico['Close'].tail(50).mean()
    
    if preco_atual < media_50:
        status = "🛒 Bom momento para comprar (Abaixo da média)"
    else:
        status = "⚖️ Preço acima da média (Aguardar)"
        
    if nome == "DÓLAR":
        mensagem += f"💵 **{nome}**: R$ {preco_atual:.2f} (Média: R$ {media_50:.2f})\nStatus: {status}\n\n"
    else:
        mensagem += f"📈 **{nome}**: {preco_atual:.2f} (Média: {media_50:.2f})\nStatus: {status}\n\n"

bot.send_message(CHAT_ID, message, parse_mode="Markdown")
print("Análise enviada para o Telegram!")
