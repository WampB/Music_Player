# Music_Player(基于Python的简易音乐播放器)
A simple GUI to play music, design your own music player!
<div id="summary">
  如果我们仅仅需要播放一些mp3文件，显然不需要安装一个几百MB音乐播放器，用一个不到600KB的Python脚本就可以很好地满足我们的需求，并且我们也不会被商用音乐播放器中充斥的大量广告和短视频影响，专心地实现单纯的听音乐的目标，何乐而不为呢？
</div><br>
<div align="center">###-------------------------------------------------------Version 0.0-------------------------------------------------------###</div>
<div id="introduction0.0">
  <p class="details" id="intro_0_1"><b>介绍一：</b><br>运行Music_Player.py即可（也可以直接双击运行“Music_Player.exe”，这是一个已经打包好的应用程序，大小不到15MB），该脚本基于Python的GUI库tkinter、音乐解析库pygame，使用pip 安装即可；</p>
  <p class="details" id="intro_0_2"><b>介绍二：</b><br>单击Select Directory按钮，选择一个包含mp3的文件夹（其他文件需要转换成mp3文件，transform.py提供了一个转换方法），该文件夹下所有的mp3文件会被导入GUI的音乐列表当中，播放按钮将被激活；</p>
  <p class="details" id="intro_0_3"><b>介绍三：</b><br>两种方式开始播放音乐，一种是单击Play按钮，默认从第一首开始播放；另一种是双击音乐列表中的曲目进行播放；开始播放后可以再次双击歌曲名称播放，若不操作，会按顺序进行播放；</p>
  <p class="details" id="intro_0_4"><b>介绍四：</b><br>单击◀键可以播放上一首歌曲，单击▶键可以播放下一首歌曲，单击Pause/Continue可以暂停/继续播放歌曲；单击Stop可以停止播放；</p>
  <p class="details" id="intro_0_5"><b>介绍五：</b><br>再次单击Select Directory可以重新选择mp3文件所在的文件夹并清空现有列表；</p>
  <p class="details" id="intro_0_6"><b>介绍六：</b><br>当前正在播放的歌曲名称会以“Playing...+歌曲名称”的形式在列表和操作栏之间显示；</p>
  <p class="details" id="intro_0_7"><b>介绍七：</b><br>上传了一些自己喜欢听的歌曲，仅作学习交流，请勿用作商业用途。</p>
</div>
<div align="center">###-------------------------------------------------------Version 0.1-------------------------------------------------------###</div>
<div id="introduction0.1">
  <p class="details" id="intro_1_1"><b>介绍一：</b><br>继承了之前版本的所有功能</p>
  <p class="details" id="intro_1_2"><b>介绍二：</b><br>增加了快捷键功能
    <ol>
      <li>面向GUI
        <ul>
          <li>Control+Return: select directory;</li>
          <li>KeyPress-Left: play previous (neighbor) song;</li>
          <li>KeyPress-Right: play next (neighbor) song;</li>
          <li>Return: play the currently selected song.</li>
        </ul>
      </li>
      <li>面向列表Listbox()
        <ul>
          <li>KeyPress-Up: move the cusor up;</li>
          <li>KeyPress-Down: move the cursor down;</li>
          <li>Return: play the song currently selected by cusor.</li>
        </ul>
      </li>
    </ol>
  </p>
  <p class="details" id="intro_1_3"><b>介绍三：</b><br>拖拽功能
    <ul>
      <li>将文件拖至快捷方式图标上即可打开GUI，点击"select directory"并选择文件夹，即可在文件夹中形成的列表中添加拖拽的mp3歌曲至列表中播放，目前仅限一首歌曲；</li>
      <li>将文件夹拖至快捷方式图标上即可打开GUI，点击"select directory"，无需选择文件夹，即可自动将选中的文件夹中所有的mp3文件解析至列表中。</li>
    </ul>
  </p>
  <p class="details" id="intro_1_4"><b>介绍四：</b><br>播放模式切换——新增了控制播放模式的控件，点击即可在顺序、随机、循环之间切换
    <ul>
      <li>order: 顺序播放；</li>
      <li>rand: 随机播放；</li>
      <li>circle: 循环播放。</li>
    </ul>
  </p>
  <p class="details" id="intro_1_5"><b>介绍五：</b><br>优化了选中模式，0.0版本中列表不会自动选中正在播放的歌曲，0.1实现了该功能，方便确定正在播放歌曲的位置</p>
</div>
