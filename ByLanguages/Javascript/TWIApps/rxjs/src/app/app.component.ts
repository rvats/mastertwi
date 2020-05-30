import { Component, OnInit, OnDestroy } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, Subject } from "rxjs";
import {
  debounceTime,
  distinctUntilChanged,
  switchMap,
  tap,
  map,
} from "rxjs/operators";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
})
export class AppComponent implements OnInit, OnDestroy {
  constructor(private http: HttpClient) {}
  searchSubject$ = new Subject<string>();
  results$: Observable<any>;

  ngOnInit() {
    this.results$ = this.searchSubject$.pipe(
      debounceTime(200),
      distinctUntilChanged(),
      tap((result) => console.log("Check Result in Init: ", result)),
      switchMap((searchString) => this.queryAPI(searchString))
    );
  }

  queryAPI(searchString) {
    console.log("queryAPI", searchString);
    return this.http
      .get(`https://www.reddit.com/r/aww/search.json?q=${searchString}`)
      .pipe(
        tap((result) => {
          console.log(
            "Check Result From QueryAPI: ",
            result["data"]["children"]
          );
        }),
        map((result) => result["data"]["children"])
      );
  }

  inputChanged($event) {
    console.log("input changed", $event);
    this.searchSubject$.next($event);
  }

  ngOnDestroy() {}
}
