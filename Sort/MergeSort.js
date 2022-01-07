/*


*/
function mergeSort(A, start, end, temp) {
  if (start >= end) {
    return;
  }
  // 处理左半区间
  mergeSort(A, start, (start + end) / 2, temp);
  // 处理右半区间
  mergeSort(A, (start + end) / 2 + 1, end, temp);
  // 合并排序数组
  merge(A, start, end, temp);
}

function merge(A, start, end, temp) {
  let middle = (start + end) / 2;
  let leftIndex = start;
  let rightIndex = middle + 1;
  let index = start;
  while (leftIndex <= middle && rightIndex <= end) {
    if (A[leftIndex] < A[rightIndex]) {
      temp[index++] = A[leftIndex++];
    } else {
      temp[index++] = A[rightIndex++];
    }
  }
  while (leftIndex <= middle) {
    temp[index++] = A[leftIndex++];
  }
  while (rightIndex <= end) {
    temp[index++] = A[rightIndex++];
  }
  for (let i = start; i <= end; i++) {
    A[i] = temp[i];
  }
}
