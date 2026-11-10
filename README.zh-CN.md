# Engineering Skills

将工程变更从设计推进到实现、验证、文档和 Git 记录的轻量 skill 组合包。
首版面向 Codex，使用普通 `SKILL.md`，不引入工作流引擎、模型服务或外部代理依赖。

## 包含什么

| Skill | 职责 |
| --- | --- |
| `engineering-workflow` | 总入口：界定范围、选择必要阶段、协调交接 |
| `highlevel-design` | HLD：架构边界、用户/逻辑/部署视图及验证约束 |
| `lowlevel-design` | LLD：文件、接口、数据、异常与测试映射 |
| `design-plan-closure-review` | 对设计和计划反复审查、修订，直到问题闭环 |
| `engineering-implement` | 按已确定的设计做最小实现 |
| `engineering-test` | 按风险选择并执行真实验证 |
| `engineering-review` | 审查代码缺陷、回归风险和测试缺口 |
| `engineering-deliver` | 更新文档、记录证据、提交本次相关 Git 变更 |

主线：范围确认 → 必要的 HLD/LLD → 设计与计划闭环 → 实现 → 测试 → 代码审查 → 文档与 Git 提交。
小修复可跳过完整 HLD/LLD，但不能把未执行的验证说成通过。
设计和计划分开：前者描述系统如何工作，后者描述按什么顺序实施。

## 安装

需要 Git 和 Python 3.10+；skill 内容本身不依赖 Python。

```sh
git clone https://github.com/Logic70/engineering-skills.git
cd engineering-skills
python scripts/install.py --dest /path/to/project/.agents/skills --dry-run
python scripts/install.py --dest /path/to/project/.agents/skills
```

Windows 下将目标换为带引号的实际路径。也可显式指定 Codex 用户级
`~/.codex/skills` 目录，Windows 建议使用完整路径。必要时重新启动代理会话以发现新 skill。
安装只复制八个 skill 目录，不覆盖已有文件；任一同名目录或文件存在就会提前停止。
已有同名 HLD/LLD 等 skill 时，先人工比较，或安装到干净的项目目录。
项目级与用户级 skill 可能互相遮蔽，应确认代理实际加载的版本。
复制中途遇到磁盘或权限错误时会报告失败，但可能留下部分目录；重试前需人工检查，
只清理确认属于该次失败安装的文件，安装器不会自动删除用户文件。
其他代理能否自动发现取决于其自身机制，本包不声称已经完成跨代理兼容性验证。

## 使用

```text
使用 $engineering-workflow，在 <仓库路径> 完成 <变更目标>。
遵守项目指令，保留无关的已有修改。
```

也可单独调用 `$engineering-test` 等。它们是代理指令，不是终端命令。
只要求设计或审查时，不自动修改业务代码或提交。
正常实现任务在没有禁止指令时包含本地 Git 提交，但 push、公开发布和外部代理委派需要明确授权。

优先复用项目已有文档、issue、PR 和测试工具；没有持久记录位置时，在仓库保存简短变更记录。
记录范围、设计结论、真实测试结果、审查结论、未解决事项和交付状态。
提交号在提交后报告或更新已有外部记录，不为把提交号写进它自身而反复提交。

## 验证与边界

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

校验覆盖包结构、本地链接、关键交接规则和安装行为，不等于真实项目的端到端验收，
也不能证明模型一定遵循指令。测试缺失和执行失败必须明确记录。
包不包含机器私有配置、凭据、调度器或 WorkflowProgram 插件代码。

详见 [设计说明](docs/design.md)、[首版验收记录](docs/verification.md)、[变更记录示例](examples/change-record.md)、
[贡献指南](CONTRIBUTING.md) 和 [MIT 许可证](LICENSE)。
