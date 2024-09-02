import OpenAI from "openai";
import { OpenAIStream, StreamingTextResponse } from "ai";

// Create an OpenAI API client (that's edge friendly!)
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// IMPORTANT! Set the runtime to edge
export const runtime = "edge";

export async function POST(req: Request) {
  const { messages } = await req.json();
  console.log('messages = ', messages);

  // Ask OpenAI for a streaming chat completion given the prompt
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    stream: true,
    messages: [
      {
        role: 'system',
        content: 'You are one of the best joke tellers in the world, in a humorous and friendly tone, but not insulting or hurtful. Your specialty is American humor in the tradition of the Marx Brothers or Woody Allen, and you are able to tell jokes of the type witty, sarcastic, silly, dark, goofy and others. The viewer user can ask you to tell a default joke at random or can give you a theme. He can also ask for a type of joke. If they ask you for things that cannot be related to jokes, politely decline and do not respond.',
      },
      ...messages,
    ],
  });

  // Convert the response into a friendly text-stream
  const stream = OpenAIStream(response);
  // Respond with the stream
  return new StreamingTextResponse(stream);
}
