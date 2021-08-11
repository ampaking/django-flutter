import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Note {
  final int? id;
  final String? note;

  Note({
    this.id,
    this.note,
  });
}

class DataState with ChangeNotifier {
  List<Note> _notes = [];
  // String urls = 'http://127.0.0.1:8000/notes/';
  String urls = 'http://10.0.2.2:8000/notes/';

  Future<void> getNotesData() async {
    http.Response responseData = await http.get(
      Uri.parse(urls),
    );
    if (responseData.statusCode == 200) {
      var data = json.decode(responseData.body) as List;
      List<Note> getNote = [];
      data.forEach((element) {
        Note singleNote = Note(
          id: element['id'],
          note: element['body'],
        );
        getNote.add(singleNote);
      });
      _notes = getNote;
      notifyListeners();
      // print(_notes[0].note);
    } else {
      print('no data found ' + responseData.statusCode.toString());
    }
  }

  List<Note> get getNote {
    return [..._notes];
  }
}
