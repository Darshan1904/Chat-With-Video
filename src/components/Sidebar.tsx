import VideoList from './VideoList';

export default function Sidebar() {
  return (
    <div className="w-64 bg-[#EDE6EF] p-4 text-center">
        <div className="flex gap-2 font-sans justify-between mb-4">
            <div className="text-xl py-2 font-bold">My Videos</div>
            <div><button className="text-4xl">+</button></div>
        </div>
      <VideoList />
    </div>
  );
}