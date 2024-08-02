const videos = [
    { title: "How to build a chat app w", duration: "10:24", date: "2023-04-12" },
    { title: "Mastering Tailwind CSS fo", duration: "45:12", date: "2023-03-28" },
    { title: "Optimizing React perform", duration: "22:38", date: "2023-02-15" },
  ];
  
  export default function VideoList() {
    return (
      <div>
        {videos.map((video, index) => (
          <div key={index} className="mb-2 p-2 text-left bg-[#F9F7FF] rounded shadow">
            <h3 className="font-semibold">{video.title}</h3>
            <p className="text-sm text-gray-500">{video.duration} - {video.date}</p>
          </div>
        ))}
      </div>
    );
  }