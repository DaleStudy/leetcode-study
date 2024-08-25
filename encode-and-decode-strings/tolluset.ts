/*
 * TC: O(nm)
 * SC: O(nm)
 * */
function encode(arr: string[]): string {
  return arr.join("🎃");
}

function decode(str: string): string[] {
  return str.split("🎃");
}
