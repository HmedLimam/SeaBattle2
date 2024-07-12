import 'package:flutter/material.dart';
import 'package:external_app_launcher/external_app_launcher.dart';
import 'package:flutter_overlay_window/flutter_overlay_window.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  if(! await FlutterOverlayWindow.isPermissionGranted()) {
    FlutterOverlayWindow.requestPermission();
  }
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sea Battle Overlay',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.lightBlueAccent),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Sea Battle Overlay'),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            ElevatedButton(onPressed: () async {
                if (await FlutterOverlayWindow.isActive()) {
                  FlutterOverlayWindow.closeOverlay();
                } else {
                  await FlutterOverlayWindow.showOverlay(height: 653, width: 370, enableDrag: true);
                }},
                child: const Text("Toggle Ships")),
            ElevatedButton(onPressed: () async { await LaunchApp.openApp(androidPackageName: 'com.byril.seabattle2');},
                child: const Text("Open Game"), style: ButtonStyle(backgroundColor: MaterialStateProperty.all(Colors.blue[700]), foregroundColor: MaterialStateProperty.all(Colors.white))),
          ],
        ),
      ),
    );
  }
}

@pragma("vm:entry-point")
void overlayMain() {
  runApp(const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: UIFleet(),

  ));
}

class UIFleet extends StatefulWidget {
  const UIFleet({super.key});

  @override
  State<UIFleet> createState() => _UIFleetState();
}

class _UIFleetState extends State<UIFleet> {
  var cells4 = 1;
  var cells3 = 2;
  var cells2 = 3;
  var cell1 = 4;

  void autoReset() {
    if (cells4==0 && cells3==0 && cells2==0 && cell1==0) {
      setState(() {
        cells4 = 1;
        cells3 = 2;
        cells2 = 3;
        cell1 = 4;
      });
    }
  }

  void destroyShip(cell) {
    switch (cell) {
      case 4:
        if (cells4-1>=0) cells4--; autoReset();
        break;
      case 3:
        if (cells3-1>=0) cells3--; autoReset();
        break;
      case 2:
        if (cells2-1>=0) cells2--; autoReset();
        break;
      case 1:
        if (cell1-1>=0) cell1--; autoReset();
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Material(color: Colors.transparent, child: Column(mainAxisAlignment: MainAxisAlignment.start, crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [ClipOval(child: Image.asset("assets/4Cells.png", width: 60,), ), ElevatedButton(onPressed: () { setState(() {destroyShip(4);}); }, style: ElevatedButton.styleFrom(padding: EdgeInsets.zero, minimumSize: Size.square(20)), child: Text("$cells4")  ) ],),
      SizedBox(height: 10,),
      Row(children: [ClipOval(child: Image.asset("assets/3Cells.png", width: 50), ), ElevatedButton(onPressed: () {setState(() {destroyShip(3);});}, style: ElevatedButton.styleFrom(padding: EdgeInsets.zero, minimumSize: Size.square(20)), child: Text("$cells3")  ) ],),
      SizedBox(height: 10,),
      Row(children: [ClipOval(child: Image.asset("assets/2Cells.png", width: 30), ),ElevatedButton(onPressed: () {setState(() {destroyShip(2);});}, style: ElevatedButton.styleFrom(padding: EdgeInsets.zero, minimumSize: Size.square(20)), child: Text("$cells2")  ) ],),
      SizedBox(height: 10,),
      Row(children: [ClipOval(child: Image.asset("assets/1Cell.png", width: 20), ), ElevatedButton(onPressed: () {setState(() {destroyShip(1);});}, style: ElevatedButton.styleFrom(padding: EdgeInsets.zero, minimumSize: Size.square(20)), child: Text("$cell1")  ) ],),
    ],));
  }
}
