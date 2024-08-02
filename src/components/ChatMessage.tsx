interface ChatMessageProps {
    user: string;
    message: string;
    time: string;
  }
  
  export default function ChatMessage({ user, message, time }: ChatMessageProps) {
    return (
      <div className="mb-4">
        <div className="flex items-center mb-1">
          <div className="w-8 h-8 bg-gray-300 rounded-full mr-2"></div>
          <span className="font-semibold">{user}</span>
          <span className="text-sm text-gray-500 ml-2">{time}</span>
        </div>
        <p className="ml-10">{message}</p>
      </div>
    );
  }