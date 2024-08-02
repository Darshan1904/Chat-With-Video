import ChatMessage from './ChatMessage';

export default function ChatArea() {
  return (
    <div className="flex-1 flex flex-col">
      <div className="bg-[#F9F7FF] p-4 shadow">
        <h2 className="text-xl font-bold">Chat with How to build a chat app with React</h2>
      </div>
      <div className="flex-1 overflow-y-auto p-4 bg-[#F9F7FF] border-l border-black/10">
        <ChatMessage user="John Doe" message="Hey everyone, can you see the video clearly? Let me know if you have any questions!" time="10:24 AM" />
        <ChatMessage user="Jane Smith" message="The video looks great! I can see and hear everything clearly." time="10:26 AM" />
        <ChatMessage user="John Doe" message="Awesome, I'm glad the video is working well. Let me know if you have any other questions!" time="10:28 AM" />
      </div>
      <div className="p-4 bg-[#F9F7FF]">
        <input type="text" placeholder="Type your message..." className="w-full p-2 border rounded" />
      </div>
    </div>
  );
}