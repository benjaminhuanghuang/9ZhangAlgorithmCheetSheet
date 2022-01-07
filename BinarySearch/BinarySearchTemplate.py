
def binary_search(self, nums, target):

  # corner case 处理
  # 这里等价于nums is None or len(nums) == 0
  if not nums:
    return -1

  start, end = 0, len(nums) - 1

  # 用start + 1 < end 而不是start < end 的目的是为了避免死循环
  # 在first position of target 的情况下不会出现死循环
  # 但是在last position of target 的情况下会出现死循环
  # 样例：nums=[1，1] target = 1
  # 为了统一模板，我们就都采用start + 1 < end，就保证不会出现死循环
  while start + 1 < end:
    # python 没有overflow 的问题，直接// 2 就可以了
    # java 和C++ 最好写成mid = start + (end - start) / 2
    # 防止在start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法overflow
    mid = (start + end) // 2
    # > , =, < 的逻辑先分开写，然后在看看= 的情况是否能合并到其他分支里
    if nums[mid] < target:
      start = mid
    elif nums[mid] == target:
      end = mid
    else:
      end = mid

  # 因为上面的循环退出条件是start + 1 < end
  # 因此这里循环结束的时候，start 和end 的关系是相邻关系（1 和2，3 和4 这种）
  # 因此需要再单独判断start 和end 这两个数谁是我们要的答案
  # 如果是找first position of target 就先看start，否则就先看end
  if nums[start] == target:
    return start
  if nums[end] == target:
    return end
  return -1
